# xscript/ui.py

import tkinter as _tk
import tkinter.ttk as _ttk
from tkinter import messagebox as _messagebox

def askyesno(message='', title='xscript'):
    return _messagebox.askyesno(message=message, title=title)

def destroy(widget):
    widget.destroy()

def Label(master, text):
    return _ttk.Label(master, text=text)

def mainloop(widget):
    widget.mainloop()

def pack(widget, anchor='', side='center', fill=''):
    widget.pack(widget, anchor=anchor, side=side, fill=fill)

def showinfo(message='', title='xscript'):
    return _messagebox.showinfo(message=message, title=title)

def title(widget, title=''):
    return widget.title(title)

def Window():
    return _tk.Tk()
