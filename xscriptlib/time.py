import time as _time

def ctime(secs=None):
    return _time.ctime(secs)

def gmtime(secs=None):
    return _time.gmtime(secs)

def localtime(secs=None):
    return _time.localtime(secs)

def sleep(secs):
    _time.sleep(secs)

def strftime(format, t=None):
    return _time.strftime(format, t)

def time():
    return _time.time()
