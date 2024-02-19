import tkinter as tk
from tkinter import ttk
from Calculate import Calculate, Model

class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculate')
        self.text = tk.StringVar()
        self.init_component()

    def init_component(self):
        self.calculator = Calculate(self)
        self.model = Model(self)

        menubar = tk.Menu(self)
        self.config(menu=menubar)
        self.menubar = tk.Menu(menubar, tearoff=0)
        self.menubar.add_command(label='History', command=lambda: self.model.history())
        self.menubar.add_separator()
        self.menubar.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='History and Exit', menu=self.menubar)

        self.entry = tk.Entry(justify='right', textvariable=self.text, font=('Monospace', 16), fg='purple', state='readonly')
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
            button = tk.Button(frame, text=keyname, command=lambda val=keyname: self.show(val), fg='purple')
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            frame.grid_rowconfigure(i // 3, weight=1)
            frame.grid_columnconfigure(i % 3, weight=1)

        button = tk.Button(frame, text='CLR', command=self.calculator.clear, fg='purple')
        button.grid(row=3, column=2, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='DEL', command=self.calculator.delete, width=1, fg='purple')
        button.grid(row=4, column=1, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        return frame

    def make_operator_pad(self) -> tk.Frame:
        """Create a frame containing buttons for operators."""
        frame = tk.Frame(self)
        operators = ['+', '-', '*', '/', '(', ')']

        for i, op in enumerate(operators):
            button = tk.Button(frame, text=op, command=lambda val=op: self.show(val), width=1, fg='purple')
            button.grid(row=i, column=0, sticky=tk.NSEW)
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='sqrt', command=lambda: self.calculator.special_op('sqrt'), fg='purple')
        button.grid(row=6, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='log', command=lambda: self.calculator.special_op('log'), fg='purple')
        button.grid(row=7, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        button = tk.Button(frame, text='=', command=self.calculator.calculate, fg='purple')
        button.grid(row=8, column=0, sticky=tk.NSEW)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        return frame

    def run(self):
        self.mainloop()
