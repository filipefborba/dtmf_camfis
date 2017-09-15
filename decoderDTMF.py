import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

duration = 5

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]