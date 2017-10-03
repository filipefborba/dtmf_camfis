from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import generate_sound as gs
from PIL import Image, ImageTk
from functools import partial
from pynput import keyboard


class EncoderDTMF(Frame):
    def __init__(self):
        self.root = Tk()
        self.gs = gs.GenerateSound()
        Frame.__init__(self)
        self.master.title("DTMF")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W + E + N + S)

        self.matriz = [[1,   2,   3],  
                       [4,   5,   6],
                       [7,   8,   9],
                       ["" ,   0,  ""]]
        self.buttons = []
        for i in range (4):
            for j in range(3):
                texto = str(self.matriz[i][j])
                self.button = Button(self, text=texto, command=partial(self.button_sound, texto) , width=7)
                self.button.grid(row=i, column=j, sticky=W)
                self.buttons.append(self.button)

        def onclick(event=None):
            if event.char != '0':
                self.buttons[int(event.char) - 1].invoke()
            elif event.char == '0':
                self.buttons[10].invoke()

        for i in range (10):
            self.root.bind(str(i), onclick)
        
    def button_sound(self,texto):
        if texto != "":
            self.gs.generate(texto)

if __name__ == "__main__":
    EncoderDTMF().mainloop()
