import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import pickle
from scipy.fftpack import fft, ifft
from scipy import signal as window

class DecoderDTMF:
    def __init__(self):
        self.fs = 44100
        self.duration = 2

    def make_plot(self,t,y):
        plt.plot(t[0:500], y[0:500])
        plt.show(block=False)
        sd.play(y, self.fs)
        sd.wait()        
        time.sleep(2)
        plt.close('all')
    
    def detect_frequencies(self):
    
    def calcFFT(signal, fs):

        N  = len(signal)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])
    
    def getTwoMax(lista):
        sort = sorted(lista)
        return sort[-1], sort[-2]

    def save_data(self,y):
        # Save a dictionary into a pickle file.
        pickle.dump( y, open( "save.p", "wb" ) )

    def main(self):
        while True:
            audio = sd.rec(int(self.duration*self.fs), self.fs, channels=1)
            sd.wait()

            y = audio[:,0]
            t = np.linspace(0,1,self.fs*self.duration)

            self.save_data(y)
            self.make_plot(t,y)

if __name__ == "__main__":
    DecoderDTMF().main()