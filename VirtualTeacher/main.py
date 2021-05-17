import wave
import numpy as np
import matplotlib.pyplot as plt

fname = 'music.wav'

with wave.open(fname, 'r') as f:
    numch       = f.getnchannels()
    samplewidth = f.getsampwidth()
    samplerate  = f.getframerate()
    numsamples  = f.getnframes()

    print('チャネル数', numch)
    print('サンプル幅', samplewidth)
    print('サンプリングレート', samplerate)
    print('サンプル数', numsamples)
    print('録音時間', numsamples / samplerate)

    buf = f.readframes(numsamples)

data = None

data = np.frombuffer(buf, dtype='int16')
print('[', end='')
for i in range(500):
    print(data[i], ',', end='')
print(']')
