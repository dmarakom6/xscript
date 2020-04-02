# xSheets/xscript/ui.py

import tkinter as _tk
import tkinter.ttk as _ttk
from tkinter import messagebox as _messagebox

def askyesno(message='', title='xscript'):
    return _messagebox.askyesno(message=message, title=title)

def destroy(widget):
    widget.destroy()

def showinfo(message='', title='xscript'):
    return _messagebox.showinfo(message=message, title=title)

def title(widget, title=''):
    return widget.title(title)

def window():
    return _tk.Tk()
