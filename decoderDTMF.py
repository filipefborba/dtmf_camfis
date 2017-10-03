import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import pickle
from scipy.fftpack import fft, ifft
from scipy import signal as window
from scipy.signal import find_peaks_cwt
import math

class DecoderDTMF:
    def __init__(self):
        self.fs = 44100
        self.duration = 1
    
    def make_dynamic_plot(self, x, y):
        # Cria plot
        plt.ion()
        fig = plt.figure("F(y)", figsize=(10,10))
        ax  = fig.add_subplot(111)
        
        # Atualiza plot
        ax.clear()
        ax.plot(x[0:3000],y[0:3000])
        fig.canvas.draw()

    def make_plot(self,t,y):
        plt.plot(t[0:500], y[0:500])
        plt.show(block=False)
        sd.play(y, self.fs)
        sd.wait()        
        time.sleep(2)
        plt.close('all')
    
    def calcFFT(self, signal):
        N  = len(signal)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])
    
    # def getTwoMax(self, lista):
    #     sort = sorted(lista)
    #     return sort[-1], sort[-2]

    def getFreqs(self, lista):
        indexes = find_peaks_cwt(lista, np.arange(1,550))
        print(indexes)
        return indexes[0], indexes[1]

    def save_data(self,y):
        # Save a dictionary into a pickle file.
        pickle.dump( y, open( "number_1.p", "wb" ) )

    def identify_number(self, low_freq, high_freq):
        range = 10
        if 1209-range <= high_freq <= 1209+range: #Coluna do 1, 4 e 7
            if 697-range <= low_freq <= 697+range:
                print("O número discado foi 1!")
            elif 770-range <= low_freq <= 770+range:
                print("O número discado foi 4!")
            elif 852-range <= low_freq <= 852+range:
                print("O número discado foi 7!")
        elif 1336-range <= high_freq <= 1336+range: #Coluna do 2, 5, 8 e 0
            if 697-range <= low_freq <= 697+range:
                print("O número discado foi 2!")
            elif 770-range <= low_freq <= 770+range:
                print("O número discado foi 5!")
            elif 852-range <= low_freq <= 852+range:
                print("O número discado foi 8!")
            elif 941-range <= low_freq <= 941+range:
                print("O número discado foi 0!")
        elif 1477-range <= high_freq <= 1477+range: #Coluna do 3, 6 e 9
            if 697-range <= low_freq <= 697+range:
                print("O número discado foi 3!")
            elif 770-range <= low_freq <= 770+range:
                print("O número discado foi 6!")
            elif 852-range <= low_freq <= 852+range:
                print("O número discado foi 9!")
        else:
            print("Bugou mein...")

    def main(self):
        while True:
            # audio = sd.rec(int(self.duration*self.fs), self.fs, channels=1)
            # sd.wait()

            # y = audio[:,0]
            t = np.linspace(0,self.duration,self.fs*self.duration)

            # self.save_data(y)
            # self.make_plot(t,y)
            y = pickle.load(open("teste.p", "rb")) #Pickle gerado a partir da onda correta do number_1

            X, Y = self.calcFFT(y)
            plt.plot(X, np.abs(Y))
            plt.grid()
            y_graph = list(np.abs(Y))
            low_freq, high_freq = self.getFreqs(y_graph)
            print("Frequência Baixa: " + str(low_freq ))
            print("Frequência Alta:  " + str(high_freq))
            self.identify_number(low_freq, high_freq)
            plt.show()

if __name__ == "__main__":
    DecoderDTMF().main()