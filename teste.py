import pickle 
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
import generate_sound as gs
import decoderDTMF

teste = pickle.load(open( "save.p", "rb" ))

def calcFFT(signal, fs):
    from scipy import signal as window

    N  = len(signal)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal)
    return(xf, yf[0:N//2])
    
def getTwoMax(lista):
    sort = sorted(lista)
    return sort[-1], sort[-2]

def main():
    generate = gs.GenerateSound()

    # number_1 = generate.generate(1)

    # Import sound as file
    y = pickle.load(open( "save.p", "rb" ))
    print(y[-10:])

    # y = number_1

    fs = 44100

    # Cacula a trasformada de Fourier do sinal
    X, Y = calcFFT(y, fs)

    ## Exibe sinal no tempo
    # plt.figure("y[n]")
    # plt.plot(y[0:500], 'X')
    # plt.grid()
    # plt.title('Audio no tempo')

    ## Exibe modulo 
    plt.figure("abs(Y[k])")
    #plt.stem(X[0:10000], np.abs(Y[0:10000]), linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.plot(X, np.abs(Y))
    plt.grid()
    plt.title('Modulo Fourier audio')
    y_graph = list(np.abs(Y))
    max_0, max_1 = getTwoMax(y_graph)
    print("Freq1: " + str(y_graph.index(max_0)))
    print("Freq2: " + str(y_graph.index(max_1)))
    ## Exibe fase
    # plt.figure("Fase(Y[k])")
    # plt.plot(X,np.angle(Y))
    # plt.grid()
    # plt.title('Modulo Fourier audio')

    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
