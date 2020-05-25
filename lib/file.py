def fileClose(fileobj):
    fileobj.close()

def fileFlush(fileobj):
    fileobj.flush()

def fileOpen(name, mode='r'):
    try:
        return open(name, mode)
    except:
        return None

def fileRead(fileobj, size=-1):
    return fileobj.read(size)

def fileWrite(fileobj, s):
    return fileobj.write(s)
