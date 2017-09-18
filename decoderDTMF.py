import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft, ifft

fs = 44100

duration = 2

def make_plot(t,y):
    plt.plot(t[0:500], y[0:500])
    plt.show(block=False)
    sd.play(y, fs)
    sd.wait()        
    time.sleep(2)
    plt.close('all')

while True:    
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]

    y = fft(y)

    t = np.linspace(0,1,fs*duration)

    make_plot(t,y)

    # fig = plt.figure()
    # plt.plot(t[0:500], y[0:500])
    # plt.grid(True)
    # plt.show()
    
    # plt.ion()
    # plt.show()
    # plt.pause(.01)
    
     