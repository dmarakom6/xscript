# xSheets/xscript/__init__.py

import xscript.file as file
import xscript.math as math
import xscript.random as random
import xscript.string as string
import xscript.turtle as turtle
import xscript.ui as ui
import xscript.util as util

def tocomplex(real=0, imag=0):
    return complex(real, imag)

def toint(n):
    return int(n)

def tofloat(n):
    return float(n)

def tolist(*n):
    return list(n)
