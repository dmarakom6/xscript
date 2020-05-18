def gets(prompt='? '):
    return input(prompt)

def getsint(prompt='int? '):
    try:
        return int(input(prompt))
    except:
        return None

def getfile(prompt='file? ', mode='r'):
    try:
        return open(input(prompt), mode)
    except:
        return None

def getsfloat(prompt='float? '):
    try:
        return float(input(prompt))
    except:
        return None

def puts(*args):
    for item in args:
        print(item, end=' ')
    else:
        print()

