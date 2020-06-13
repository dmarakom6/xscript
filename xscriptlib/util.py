import builtins as _builtins

def chr(i):
    try:
        return _builtins.chr(i)
    except:
        return None

def divmod(a, b):
    try:
        return _builtins.divmod(a, b)
    except:
        return None

def hex(x):
    try:
        return _builtins.hex(x)
    except:
        return None

def gets(prompt='? '):
    return input(prompt)

def getsInt(prompt='int? '):
    try:
        return int(input(prompt))
    except:
        return None

def getFile(prompt='file? ', mode='r'):
    try:
        return open(input(prompt), mode)
    except:
        return None

def getsFloat(prompt='float? '):
    try:
        return float(input(prompt))
    except:
        return None

def oct(x):
    try:
        return _builtins.oct(x)
    except:
        return None

def ord(c):
    try:
        return _builtins.ord(c)
    except:
        return None

def pow(base, exp, mod=None):
    try:
        return _builtins.pow(base, exp, mod)
    except:
        return None

def puts(*args):
    for item in args:
        print(item, end=' ')
    else:
        print()

def round(number, ndigits):
    try:
        return _builtins.round(number,ndigits)
    except:
        return None

