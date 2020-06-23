# xscript/xIDElib/ui.py

import os.path as path
import sidebar
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

class IDEWin():

    def __init__(self, argv):
        self.win = tk.Tk()
        self.initUI()
        if len(argv) == 1:
            self.win.title('xIDE - [NEW]')
        elif self.isfile(argv[1]):
            self.win.title('xIDE - %s' % argv[1])
            self.file = argv[1]
        else:
            self.win.title('xIDE')
            messagebox.showerror(title='xIDE', message="No such file: '%s'" % argv[1], parent=self.win)

    def initUI(self):
        pass
