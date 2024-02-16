import tkinter as tk
from tkinter import ttk, Label


#TODO Keypad should extend Frame so that it is a container
class Keypad(tk.Frame):

    def __init__(self, parent, keynames=list, columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        self.column = columns
        self.keyname = keynames
        self.text = tk.StringVar()
        self.init_components(columns)
        # keynames and columns

    def show(self, value):
        current_text = self.text.get()
        self.text.set(current_text + value)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """

        keys = list('789456123 0.')
        for i, keyname in enumerate(keys):
            button = tk.Button(self, text=keyname, command=lambda val=keyname: self.show(val))
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            self.grid_rowconfigure(i // self.column, weight=1)
            self.grid_columnconfigure(i % 3, weight=1)
        # layout keypad and operators as if they were simple components
        # use any layout that works.

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for child in self.winfo_children():
            child.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        keypad['foreground'] = 'blue'
        keypad['font'] = ('Monospace', 16)

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        pass

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for child in self.winfo_children():
            child.configure(cnf, **kwargs)


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Calculator")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    root.mainloop()