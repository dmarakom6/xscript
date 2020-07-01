# xscript/kvfile.py
# key-value file read and write

from os import linesep

class ReadKVFile():

    def __init__(self, name):
        self.kvfile = open(name, 'r+')
        self.kv = {}

    def read(self):
        self.kv = {}
        for line in self.kvfile.readlines():
            if line == linesep:
                pass
            elif line[0] == '#':
                pass
            else:
                k, v = line.split(':', 1)
                k, v = k.strip(), v.strip()
                self.kv[k] = v

    def close(self):
        self.kvfile.close()
