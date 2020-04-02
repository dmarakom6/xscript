# xSheets/xscript/file.py

def fileclose(fileobj):
    fileobj.close()

def fileflush(fileobj):
    fileobj.flush()

def fileopen(name, mode='r'):
    return open(name, mode)

def fileread(fileobj, size=-1):
    return fileobj.read(size)

def filewrite(fileobj, s):
    return fileobj.write(s)
