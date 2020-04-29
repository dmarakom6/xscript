# xscript/lib/time.py

import time as _time

def ctime():
    _time.ctime()

def sleep(n):
    _time.sleep(float(n))

def time():
    return _time.time()
