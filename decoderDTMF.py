import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import pickle
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

def save_data(y):
    # Save a dictionary into a pickle file.
    pickle.dump( y, open( "save.p", "wb" ) )

while True:    
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]

    t = np.linspace(0,1,fs*duration)

    save_data(y)
    make_plot(t,y)

    # fig = plt.figure()
    # plt.plot(t[0:500], y[0:500])
    # plt.grid(True)
    # plt.show()
    
    # plt.ion()
    # plt.show()
    # plt.pause(.01)
    
     