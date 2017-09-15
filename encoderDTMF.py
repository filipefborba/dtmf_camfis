import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

#fs = 44100
dtmf_table = {
    'number_1' : [1209,697]
    'number_2' : [1336,697]
    'number_3' : [1447,697]
    'A'        : [1633,697]
    'number_4' : [1209,770]
    'number_5' : [1336,770]
    'number_6' : [1447,770]
    'B'        : [1633,770]
    'number_7' : [1209,852]
    'number_8' : [1336,852]
    'number_9' : [1447,852]
    'C'        : [1633,852]
    '*'        : [1209,941]
    'number_0' : [1336,941]
    '#'        : [1447,941]
    'D'        : [1633,941]}
    
for i in range(360):
    number_1.append(np.sin(i))

y = number_1
# reproduz o som
#sd.play(y, fs)

# aguarda fim da reprodução
#sd.wait()

t = np.arange(0.0, 1.0, 0.01)

plt.plot(t, np.sin(2*np.pi*t))
plt.grid(True)
plt.title('A sine wave or two')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude da Onda (m)')
plt.show()