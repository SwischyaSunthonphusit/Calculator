import tkinter as tk
from tkinter import ttk
from keypad import Keypad
from Calculate import Calculate
import math


class CalculatorUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.text = tk.StringVar()
        self.init_component()

    def init_component(self):
        self.entry = tk.Entry(justify='right', textvariable=self.text, font=('Monospace', 16), fg='yellow')
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
        keys = list('789456123 0.')
        for i, keyname in enumerate(keys):
            button = tk.Button(frame, text=keyname, command=lambda val=keyname: self.show(val))
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            frame.grid_rowconfigure(i // 3, weight=1)
            frame.grid_columnconfigure(i % 3, weight=1)
        return frame

    def make_operator_pad(self) -> tk.Frame:
        """Create a frame containing buttons for operators."""
        frame = tk.Frame(self)
        operators = ['+', '-', '*', '/',]

        for i, op in enumerate(operators):
            button = tk.Button(frame, text=op, command=lambda val=op: self.show(val))
            button.grid(row=i, column=0, sticky=tk.NSEW, padx=2, pady=2)
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(0, weight=1)
        button = tk.Button(frame, text='=', command=Calculate.calculate())
        button.grid(row=4, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        return frame

    def run(self):
        self.mainloop()