import wave, struct, math
import sounddevice as sd
from scipy import signal as sg
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

'''
- Mensagem :
    - ler dois arquivos .wav, essas serão as mensagens (m1(t), m2(t)) a serem transmitidas.
- Portadoras :
    - receber como parâmetro as frequências das portadoras (f1, f2)
- Modulação :
    - modular em AM (ou FM) as mensagens m1 e m2 nas frequências f1 e f2
- Transmissão :
    - transmitir o sinal modulado em áudio resultante de m1,f1 e m2,f2
- Exibir :
    - os sinais (mensagens) a serem transmitidas no tempo
    - os Fourier dos sinais (frequência)
    - as portadoras no tempo
    - as mensagens moduladas no tempo
    - os Fourier das mensagens moduladas (frequência)
'''

class Transmitter:
    def __init__(self):
        self.fcut = 4000
        self.fs = 44100
        self.m1 = "raphorba.wav"
        self.m2 = "trabson.wav"

    def calcFFT(self, signal):
        N  = len(signal)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, yf[0:N//2])
    
    def make_plot(self, x, y):
        # y_db = []
        fig = plt.figure()
        # ymax = 20000
        # for value in y:
        #     new_value = 10*math.log(value/ymax)
        #     y_db.append(new_value)

        # plt.plot(x, y_db)
        plt.plot(x, y)
        plt.axis([0,8000,0,max(y)+10])
        plt.grid(True)
        plt.ylabel("Decibéis (dB)")
        plt.xlabel("Frequência (Hz)")
        plt.title("Modulação AM")
        plt.show()

    def LPF(self, signal, cutoff_hz, fs):
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return(sg.lfilter(taps, 1.0, signal))

    def play(self, audio, samplerate):
        sd.play(audio, samplerate)
        sd.wait()

    def main(self):
        #Importando os audios
        m1, m1_samplerate = sf.read(self.m1)
        m2, m2_samplerate = sf.read(self.m2)
        print("Áudio: " + self.m1)
        print("Tamanho do áudio: ", len(m1))
        print("Samplerate do áudio: ", m1_samplerate)
        print("Áudio: " + self.m2)
        print("Tamanho do áudio: ", len(m2))
        print("Samplerate do áudio: ", m2_samplerate)

        #Reproduzindo os audios
        # self.play(m1, m1_samplerate)
        # self.play(m2, m2_samplerate)

        #Aplicando o filtro passa baixas
        m1_filtrado = self.LPF(m1, self.fcut, m1_samplerate)
        m2_filtrado = self.LPF(m2, self.fcut, m2_samplerate)

        #Aplicando o Fourier nos sinais
        m1_fftx, m1_ffty = self.calcFFT(m1_filtrado)
        m2_fftx, m2_ffty = self.calcFFT(m2_filtrado)

        #Plotando o Fourier dos sinais
        self.make_plot(m1_fftx, np.abs(m1_ffty))
        self.make_plot(m2_fftx, np.abs(m2_ffty))

        #Reproduzindo os novos audios
        self.play(m1_filtrado, m1_samplerate)
        self.play(m2_filtrado, m2_samplerate)

if __name__ == "__main__":
    Transmitter().main()
