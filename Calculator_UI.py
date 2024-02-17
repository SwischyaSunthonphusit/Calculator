import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from math import sqrt
import pygame

class CalculatorUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Calculate')
        self.text = tk.StringVar()
        self.text_history = []
        self.init_component()

    def init_component(self):
        self.entry = tk.Entry(justify='right', textvariable=self.text, font=('Monospace', 16), fg='black')
        self.entry.pack(side=tk.TOP, expand=True, fill=tk.BOTH, anchor=tk.NW)

        keypad = self.make_keypad()
        operator_pad = self.make_operator_pad()
        keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        operator_pad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def show(self, value):
        current_text = self.text.get()
        self.text.set(current_text + value)

    def make_keypad(self) -> tk.Frame:
        """Create a frame containing buttons for the numeric keys."""
        frame = tk.Frame(self)
        keys = list('789456123.0')
        for i, keyname in enumerate(keys):
            button = tk.Button(frame, text=keyname, command=lambda val=keyname: self.show(val))
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            frame.grid_rowconfigure(i // 3, weight=1)
            frame.grid_columnconfigure(i % 3, weight=1)

        button = tk.Button(frame, text='CLR', command=self.clear)
        button.grid(row=3, column=2, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='HSTR', command=self.history, width=1)
        button.grid(row=4, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='DEL', command=self.delete, width=1)
        button.grid(row=4, column=1, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        return frame

    def make_operator_pad(self) -> tk.Frame:
        """Create a frame containing buttons for operators."""
        frame = tk.Frame(self)
        operators = ['+', '-', '*', '/', '(', ')']

        for i, op in enumerate(operators):
            button = tk.Button(frame, text=op, command=lambda val=op: self.show(val), width=1)
            button.grid(row=i, column=0, sticky=tk.NSEW)
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='sqrt', command=self.sqrt, width=1)
        button.grid(row=6, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='=', command=self.calculate)
        button.grid(row=7, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        return frame

    def calculate(self):
        get_text = self.text.get()
        try:
            self.result = str(eval(str(self.text.get())))
        except Exception as e:
            self.entry.config(fg='red')
            pygame.mixer.init()
            pygame.mixer.music.load('/Users/swischyasunthonphusit/Loud Incorrect Buzzer Lie Sound Effect.mp3')
            pygame.mixer.music.play()
        self.text_history.append([get_text, self.result])
        self.clear()
        self.show(self.result)

    def clear(self):
        self.text.set(' ')
        self.entry.config(fg='black')


    def history(self):
        self.clear()
        for text in self.text_history:
            self.text.set(f'{text[0]} = {text[1]}')

    def delete(self):
        if self.text.get()[-1] == 't':
            self.text.set(self.text.get()[:-3])
        self.text.set(self.text.get()[:-1])

    def sqrt(self):
        if [*str(self.text.get())][-1] in ['+', '-', '*', '/']:
            self.text.set(f'{self.text.get()}sqrt(')
        else:
            self.text.set(f'sqrt({self.text.get()})')

    def run(self):
        self.mainloop()