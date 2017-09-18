import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import math

class GenerateSound:
    def __init__(self):
        self.fs = 44100
        self.dtmf_table = {
        'number_1' : [1209,697],
        'number_2' : [1336,697],
        'number_3' : [1477,697],
        'A'        : [1633,697],
        'number_4' : [1209,770],
        'number_5' : [1336,770],
        'number_6' : [1477,770],
        'B'        : [1633,770],
        'number_7' : [1209,852],
        'number_8' : [1336,852],
        'number_9' : [1477,852],
        'C'        : [1633,852],
        '*'        : [1209,941],
        'number_0' : [1336,941],
        '#'        : [1477,941],
        'D'        : [1633,941]}
        self.time = np.linspace(0,1,self.fs)

    def generate(self, numero):
        numero = 'number_' + str(numero)
        freq1a = self.dtmf_table[numero][0]
        sin1a = np.sin(2*math.pi*self.time*freq1a)
        freq1b = self.dtmf_table[numero][1]
        sin1b = np.sin(2*math.pi*self.time*freq1b)
        sin1 = sin1a + sin1b

        sd.play(sin1, self.fs)
        sd.wait()

        # plt.plot(self.time[0:1000], sin1[0:1000])
        # plt.grid(True)
        # plt.show()



