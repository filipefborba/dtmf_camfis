import wave, struct, math
import sounddevice as sd
from scipy import signal as sg
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import transmissor

'''
- Portadoras :
    - receber como parâmetro as frequências das portadoras (f1, f2)
- Sinal :
    - receber via microfone o sinal (y(t)) transmitido pelo computador com o transmissor.
- Demodulação :
    - demodular o sinal AM (ou FM) recebido em :
        - m1 e m2
- Mensagens
    - salvar as mensagens m1 e m2 em arquivos wav
    - reproduzir os sons recuperados.
- Exibir :
    - o sinal y(t) no tempo
    - o sinal y(t) na frequência
    - os sinais (mensagens) recuperados (no tempo)
    - os sinais (mensagens) recuperados (na frequência)
'''

class Receiver:
    def __init__(self):
        self.fcut = 4000
        self.fs = 44100
        self.fc1 = 5000
        self.fc2 = 15000
        self.audio_recebido = "recebido.wav"
        self.m1 = "trabson_recuperado.wav"
        self.m2 = "raphorba_recuperado.wav"

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
        ripple_db = 8.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return(sg.lfilter(taps, 1.0, signal))

    def rec(self, duration):
        audio = sd.rec(int(duration*self.fs), self.fs, channels=1)
        sd.wait()
        return audio

    def play(self, audio, samplerate):
        sd.play(audio, samplerate)
        sd.wait()
    
    def saveWav(self, dir, audio, samplerate):
        sf.write(dir, audio, samplerate)
        print("Áudio: " + dir)
        print("Tamanho do áudio: ", len(audio))
        print("Samplerate do áudio: ", samplerate)

    def main(self):
        #Gravando o Áudio
        audio = self.audio_recebido
        # teste = transmissor.Transmitter()
        # audio = teste.main()

        #Fourier do sinal recebido
        audio_fftx, audio_ffty = self.calcFFT(audio)

        #Plotando o fourier dos sinal recebidos
        # self.make_plot(audio_fftx, np.abs(audio_ffty))
        
        #---------------------------------
        #Reconstrução das portadoras originais
        t = np.linspace(0, len(audio)/self.fs, len(audio))
        port1 = np.sin(2*np.pi*self.fc1*t)
        port2 = np.sin(2*np.pi*self.fc2*t)
        #---------------------------------

        #Demodulando o primeiro som
        m1_linha = audio*port1
        m1_linha_fftx, m1_linha_ffty = self.calcFFT(m1_linha)
        self.make_plot(m1_linha_fftx, np.abs(m1_linha_ffty))

        m1 = self.LPF(m1_linha, self.fcut, self.fs)
        m1_fftx, m1_ffty = self.calcFFT(m1)
        self.make_plot(m1_fftx, np.abs(m1_ffty))
        self.play(m1, self.fs)
        
        #---------------------------------
        #Demodulando o segundo som
        m2_linha = audio*port2 
        m2_linha_fftx, m2_linha_ffty = self.calcFFT(m2_linha)
        self.make_plot(m2_linha_fftx, np.abs(m2_linha_ffty))

        m2 = self.LPF(m2_linha, self.fcut, self.fs)
        m2_fftx, m2_ffty = self.calcFFT(m2)
        self.make_plot(m2_fftx, np.abs(m2_ffty))
        self.play(m2, self.fs)
        # plt.figure("bruto")
        # plt.plot(tmp)

        # plt.figure("filtrado")
        # plt.plot(m2)
        # plt.show()
        #----------------------------------

        Salvando os sinais recuperados
        self.saveWav(self.m1, m1, m1_samplerate)
        self.saveWav(self.m2, m2, m2_samplerate)

if __name__ == "__main__":
    Receiver().main()
