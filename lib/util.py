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

def puts(*args):
    for item in args:
        print(item, end=' ')
    else:
        print()

