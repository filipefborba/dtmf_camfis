import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import pickle
from scipy.fftpack import fft, ifft
from scipy import signal as window
from scipy.signal import find_peaks_cwt
from itertools import combinations
import math

class DecoderDTMF:
    def __init__(self):
        self.fs = 44100
        self.duration = 1
        self.file = ""

    def setFile(self, fileDir):
        self.file = fileDir
    
    def make_dynamic_plot(self, x, y):
        y_db = []
        ymax = 20000
        for value in y:
            new_value = 10*math.log(value/ymax)
            y_db.append(new_value)
        # Cria plot
        plt.ion()
        fig = plt.figure("DTMF", figsize=(6,6))
        ax  = fig.add_subplot(111)
        
        # Atualiza plot
        ax.clear()
        ax.plot(x,y_db)
        ax.grid(True)
        ax.set_ylabel("Decibéis (dB)")
        ax.set_xlabel("Frequência (Hz)")
        ax.set_title("Identificação DTMF")
        fig.canvas.draw()

    def make_plot(self, x, y):
        y_db = []
        ymax = 20000
        for value in y:
            new_value = 10*math.log(value/ymax)
            y_db.append(new_value)
        plt.plot(x, y)
        plt.grid(True)
        plt.ylabel("Decibéis (dB)")
        plt.xlabel("Frequência (Hz)")
        plt.title("Identificação DTMF")
        plt.show()
        

    def save_data(self,y):
        # Save a dictionary into a pickle file.
        pickle.dump( y, open( "number_1.p", "wb" ) )
    
    def calcFFT(self, signal):
        N  = len(signal)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])

    def getFreqs(self, lista):
        cleared_indexes = []
        indexes = find_peaks_cwt(lista, np.arange(1,200))
        indexes = indexes//2
        for value in list(indexes):
            if 650 <= value <= 1700:
                cleared_indexes.append(value)
        return cleared_indexes

    def identify_number(self, freq_list):
        range = 5
        freq_list = freq_list[::-1]
        print(freq_list)
        for combo in combinations(freq_list, 2):
            high_freq, low_freq = combo
            if 1209-range <= high_freq <= 1209+range:
                if 697-range <= low_freq <= 697+range:
                    print("O número discado foi 1!")
                    break
                elif 770-range <= low_freq <= 770+range:
                    print("O número discado foi 4!")
                    break
                elif 852-range <= low_freq <= 852+range:
                    print("O número discado foi 7!")
                    break
            elif 1336-range <= high_freq <= 1336+range:
                if 697-range <= low_freq <= 697+range:
                    print("O número discado foi 2!")
                    break
                elif 770-range <= low_freq <= 770+range:
                    print("O número discado foi 5!")
                    break
                elif 852-range <= low_freq <= 852+range:
                    print("O número discado foi 8!")
                    break
                elif 941-range <= low_freq <= 941+range:
                    print("O número discado foi 0!")
                    break
            elif 1477-range <= high_freq <= 1477+range:
                if 697-range <= low_freq <= 697+range:
                    print("O número discado foi 3!")
                    break
                elif 770-range <= low_freq <= 770+range:
                    print("O número discado foi 6!")
                    break
                elif 852-range <= low_freq <= 852+range:
                    print("O número discado foi 9!")
                    break

        print("Frequência Alta: " + str(high_freq))
        print("Frequência Baixa: " + str(low_freq))
        return high_freq, low_freq

    def main(self):
        while True:
            # audio = sd.rec(int(self.duration*self.fs), self.fs, channels=1)
            # sd.wait()
            # y = audio[:,0]
            # self.save_data(y)
            # self.make_plot(t,y)
            # t = np.linspace(0,self.duration,self.fs*self.duration)

            y = pickle.load(open(self.file, "rb"))

            X, Y = self.calcFFT(y)
            y_graph = list(np.abs(Y))
            freq_list = self.getFreqs(y_graph)
            self.identify_number(freq_list)
            self.make_plot(X, np.abs(Y))
    
    def onthefly(self):
        while True:
            t = np.linspace(0,self.duration,self.fs*self.duration)
            audio = sd.rec(int(self.duration*self.fs), self.fs, channels=1)
            sd.wait()
            y = audio[:,0]
            X, Y = self.calcFFT(y)
            y_graph = list(np.abs(Y))
            freq_list = self.getFreqs(y_graph)
            self.save_data(y)
            self.identify_number(freq_list)
            self.make_dynamic_plot(X, np.abs(Y))

if __name__ == "__main__":
    DecoderDTMF().main()