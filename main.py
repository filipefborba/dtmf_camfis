from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.messagebox import showerror
import generate_sound as gs
from PIL import Image, ImageTk
from functools import partial
from pynput import keyboard
import tkinter as tk
import encoderDTMF
import decoderDTMF

class Screen:
    def __init__(self):
        self.btnfn = None
        self.startTrigger = False
        self.fileDir = None
        self.decoderdtmf = decoderDTMF.DecoderDTMF()

        print('Screen Started')
        self.window = tk.Tk()
        self.window.geometry('250x200')
        self.window.title('DTMF')
        self.window.resizable(0, 0)
        for i in range(2):
            self.window.rowconfigure(i, minsize=50)

        self.window.columnconfigure(0, minsize=250)
        self.window.configure(bg='#14A1CC')

        self.title = tk.Label(self.window)
        self.title.configure(text='Raphorba',fg='white',bg='#006400')
        self.title.configure(font=('calibri', 15, 'bold'))
        self.title.grid(row=0, rowspan=1, column=0, sticky='nsew')

        self.title2 = tk.Label(self.window)
        self.title2.configure(text= 'Selecione seu papel',fg='white',bg='#14A1CC')
        self.title2.configure(font=('calibri', 13, 'bold'))
        self.title2.grid(row=1, rowspan=1, column=0, sticky='nsew')

        self.encoderButton = tk.Button(self.window)
        self.encoderButton.configure(text='Encoder', command=self.setEncoder,highlightbackground='#006400')
        self.encoderButton.configure(font=('pixelmix', 11))
        # self.clientButton.grid(row=6, rowspan=1, column=0, sticky='nsew')
        self.encoderButton.place(rely=1.0, relx=1.0, x=-35, y=-40, anchor='se')

        self.decoderButton = tk.Button(self.window)
        self.decoderButton.configure(text='Decoder', command=self.setDecoder)
        self.decoderButton.configure(font=('pixelmix', 11),highlightbackground='#006400',padx=20)
        self.decoderButton.place(rely=1.0, relx=1.0, x=-225, y=-40, anchor='sw')

    def setEncoder(self):
        self.hideRoleButtons()
        self.window.destroy()
        encoderDTMF.EncoderDTMF()

    def setDecoder(self):
        self.hideRoleButtons()
        self.updateText("Selecione o modo do Decoder")
        self.onTheFlyDecoderButton = tk.Button(self.window)
        self.onTheFlyDecoderButton.configure(text='On The Fly', command=self.onTheFlyDecoder)
        self.onTheFlyDecoderButton.configure(font=('pixelmix', 11),highlightbackground='#006400',padx=39.5)
        self.onTheFlyDecoderButton.place(rely=1.0, relx=1.0, x=-50, y=-20, anchor='se')

        self.pickFileDecoderButton = tk.Button(self.window)
        self.pickFileDecoderButton.configure(text='Escolher Arquivo', command=self.pickFileDecoder)
        self.pickFileDecoderButton.configure(font=('pixelmix', 11),highlightbackground='#006400',padx=20)
        self.pickFileDecoderButton.place(rely=1.0, relx=1.0, x=-50, y=-60, anchor='se')
    
    def onTheFlyDecoder(self):
        self.hideDecoderButtons()
        self.updateText("Modo On-The-Fly")
        self.decoderdtmf.onthefly()
    
    def pickFileDecoder(self):
        self.hideDecoderButtons()
        self.insertButton = tk.Button(self.window, text='Escolher', command=self.askopenfile)
        self.insertButton.configure(fg='black',bg='#1e9622',highlightbackground='#006400')
        self.insertButton.grid(row=4, rowspan=1, column=0, sticky='nsew')

    def hideRoleButtons(self):
        self.decoderButton.destroy()
        self.encoderButton.destroy()
    
    def hideDecoderButtons(self):
        self.onTheFlyDecoderButton.destroy()
        self.pickFileDecoderButton.destroy()
        
    def updateText(self,txt):
        self.title2.configure(text=txt)

    def setFn(self,fn):
        self.btnfn = fn

    def askopenfile(self):
        fileName = filedialog.askopenfilename(initialdir = "/", title = "Select file",filetypes = (("pickle files","*.p"), ("all files","*.*")))
        self.fileDir = fileName
        split = fileName.split('/')
        self.insertButton.configure(text='Arquivo: ' + split[len(split) - 1])
        if fileName == '':
            self.fileDir = None
            print('Nenhum arquivo selecionado... Aguardando seleção')
        else:
            self.decoderdtmf.setFile(self.fileDir)
            self.sendButton = tk.Button(self.window,command=lambda: self.decoderdtmf.main())
            self.sendButton.configure(text='Enviar',fg='white',bg='#006400',highlightbackground='#006400',font=('calibri', 15, 'bold'))
            self.sendButton.place(rely=1.0, relx=1.0, x=-162.5, y=-5, anchor='sw')


    def getFileDirectory(self):
        while self.fileDir == None:
            time.sleep(1)
        return self.fileDir

    def start(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self):
        self.window.destroy()
        raise SystemExit

Screen().start()