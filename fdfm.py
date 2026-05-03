import numpy as np
import soundfile as sf
from scipy.signal import resample
from flask import Flask, request, render_template_string

# ---------- CONFIG ----------
def load_config():
    cfg = {}
    with open("fm_config.d") as f:
        for l in f:
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            k, v = l.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg

cfg = load_config()

LEFT = cfg["audio_left"]
RIGHT = cfg["audio_right"]
SR = int(cfg["sample_rate"])
DEV = float(cfg["frequency_deviation"])
OUT = cfg["iq_output_file"]

# ---------- AUDIO ----------
L, lr = sf.read(LEFT)
R, rr = sf.read(RIGHT)

L = resample(L, int(len(L) * SR / lr))
R = resample(R, int(len(R) * SR / rr))

L /= np.max(np.abs(L))
R /= np.max(np.abs(R))

# Stereo multiplex
LplusR = (L + R) / 2
LminusR = (L - R) / 2

# Time
t = np.arange(len(LplusR)) / SR

# Stereo pilot (19kHz) and subcarrier (38kHz)
pilot = 0.1 * np.sin(2 * np.pi * 19000 * t)
stereo = LminusR * np.cos(2 * np.pi * 38000 * t)

# Composite signal
composite = LplusR + stereo + pilot

# FM Modulation
phase = 2 * np.pi * DEV * np.cumsum(composite) / SR
fm = np.exp(1j * phase)

iq = np.column_stack((fm.real, fm.imag))
iq.astype(np.float32).tofile(OUT)

# ---------- UI ----------
app = Flask(__name__)

@app.route("/")
def ui():
    return render_template_string("""
    <h2>FM Stereo Transmitter</h2>
    <p>Output file: {{out}}</p>
    <p>Carrier: 100 MHz</p>
    <p>Status: IQ generated</p>
    """, out=OUT)

app.run(port=5000)
