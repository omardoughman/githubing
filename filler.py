import re

def load_h_config(path):
    cfg = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("#define"):
                continue
            parts = line.split(None, 2)
            if len(parts) < 3:
                continue
            key = parts[1]
            value = parts[2].strip().strip('"')
            cfg[key] = value
    return cfg

cfg = load_h_config("fm_config.h")

AUDIO_L = cfg["AUDIO_LEFT_FILE"]
AUDIO_R = cfg["AUDIO_RIGHT_FILE"]
CARRIER = int(cfg["CARRIER_FREQUENCY"])
SR = int(cfg["SAMPLE_RATE"])
DEV = int(cfg["FREQ_DEVIATION"])
OUT = cfg["IQ_OUTPUT_FILE"]
