import tkinter as tk
from tkinter import ttk
import pygame
from math import sqrt, log


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
        self.ui.entry.config(fg='black')

    def history(self):
        self.history_combobox = tk.Tk()
        self.history_combobox.title('Calculate History')
        self.history_combobox = ttk.Combobox()
        for text in self.text_history:
            self.history_combobox['values'] = [f'{text[0]} = {text[1]}']
            self.history_combobox.pack(pady=10)
            self.history_combobox.bind("<<ComboboxSelected>>", self.ui.text.set(f'{text[0]} = {text[1]}'))

    def delete(self):
        get_text = self.ui.text.get()
        if get_text[-1] == '(' and get_text[-2] == 'g':
            self.ui.text.set(get_text[:-3])
        if get_text[-1] == '(' and get_text[-2] == 't':
            self.ui.text.set(get_text[:-4])
        self.ui.text.set(get_text[:-1])

    def special_op(self, value):
        if [*str(self.ui.text.get())][-1] in ['+', '-', '*', '/']:
            self.ui.text.set(f'{self.ui.text.get()}{value}(')
        else:
            self.ui.text.set(f'{value}({self.ui.text.get()})')
