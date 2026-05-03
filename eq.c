from pedalboard import Pedalboard, EQ
from pedalboard.io import AudioFile

board = Pedalboard([EQ(low_shelf_gain_db=6)])

with AudioFile('input.wav') as f:
    audio = f.read(f.frames)
    sr = f.samplerate

processed = board(audio, sr)

with AudioFile('out.wav', 'w', sr, processed.shape[0]) as f:
    f.write(processed)
