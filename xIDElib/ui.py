# xscript/xIDElib/ui.py

import os.path as path
import sidebar
import tkinter as tk
import tkinter.ttk as ttk

class IDEWin():

    def __init__(self, argv):
        self.win = tk.Tk()
        if len(argv) == 1:
            self.win.title('xIDE - [NEW]')
        elif self.isfile(argv[1]):
            self.dirSideBar = False
            self.win.title('xIDE - %s' % argv[1])
        else:
            pass
        self.initUI()
