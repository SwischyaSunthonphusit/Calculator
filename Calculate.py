import tkinter as tk
from tkinter import ttk
import pygame
from math import sqrt, log10, log2, exp, log


class Calculate():
    def __init__(self, ui):
        self.ui = ui
        self.text_history = []

    def calculate(self):
        get_text = self.ui.text.get()
        try:
            self.result = str(eval(str(get_text)))
        except Exception as e:
            self.ui.entry.config(fg='red')
            pygame.mixer.init()
            pygame.mixer.music.load('/Users/swischyasunthonphusit/Calculator/Loud Incorrect Buzzer Lie Sound Effect.mp3')
            pygame.mixer.music.play()
        self.text_history.append([get_text, self.result])
        self.clear()
        self.ui.show(self.result)

    def clear(self):
        self.ui.text.set(' ')
        self.ui.entry.config(fg='purple')

    def delete(self):
        if self.ui.text.get()[-1] == '(' and self.ui.text.get()[-2] == 'g':
            self.ui.text.set(self.ui.text.get()[:-3])
        if self.ui.text.get()[-1] == '(' and self.ui.text.get()[-2] == 'p':
            self.ui.text.set(self.ui.text.get()[:-3])
        if self.ui.text.get()[-1] == '(' and self.ui.text.get()[-2] == 't':
            self.ui.text.set(self.ui.text.get()[:-4])
        if [self.ui.text.get()[-1] == '(' and self.ui.text.get()[-2] == 'n']:
            self.ui.text.set(self.ui.text.get()[:-2])
        self.ui.text.set(self.ui.text.get()[:-1])

    def special_op(self, value):
        if [*str(self.ui.text.get())][-1] in ['+', '-', '*', '/']:
            self.ui.text.set(f'{self.ui.text.get()}{value}(')
        else:
            self.ui.text.set(f'{value}({self.ui.text.get()})')

    def history(self):
        self.history_window = tk.Toplevel()
        self.history_window.title('Calculate History')
        self.history_combobox = ttk.Combobox(self.history_window)
        history_values = []
        for text in self.text_history:
            history_values.append(f'{text[0]} = {text[1]}')
        self.history_combobox['values'] = history_values
        self.history_combobox.pack(pady=10)
        get_history = self.history_combobox.get()
        self.history_combobox.bind("<<ComboboxSelected>>", self.ui.text.set(str(get_history)))

