import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100

duration = 5

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]

sd.play(y, fs)
sd.wait()