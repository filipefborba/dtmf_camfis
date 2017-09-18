import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import math
import generate_sound as generate
from pynput import keyboard
import tkinter  as tk

generate = generate.GenerateSound()

# number1 = generate.generate(1)

def on_press(key):
    try:
        for i in range(0,10):
            if key.char == str(i):
                generate.generate(i)    
    except AttributeError:
        return 'AttributeError'

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()