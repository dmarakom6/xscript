# xscript/ui.py

import tkinter as _tk
import tkinter.ttk as _ttk
from tkinter import messagebox as _messagebox

def askyesno(message='', title='xscript'):
    return _messagebox.askyesno(message=message, title=title)

def Button(master):
    return _ttk.Button(master)

def configure(widget, item, value):
    widget[item] = value

def destroy(widget):
    widget.destroy()

def Label(master):
    return _ttk.Label(master)

def mainloop(widget):
    widget.mainloop()

def pack(widget, anchor=None, side=None, fill=None):
    widget.pack(widget, anchor=anchor, side=side, fill=fill)

def showinfo(message='', title='xscript'):
    return _messagebox.showinfo(message=message, title=title)

def title(widget, title=''):
    return widget.title(title)

def Window():
    return _tk.Tk()
