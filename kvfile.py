# xscript/kvfile.py
# key-value file read and write

from os import linesep

class KVFile():

    def __init__(self, name):
        self.kvfile = open(name, 'r+')
        self.kv = {}

    def get(self, name):
        if name in self.kv:
            return self.kv[name]
        else:
            return None

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

    def write(self, k, v):
        self.kv[k] = v

    def close(self):
        self.kvfile.seek(0)
        for k, v in self.kv.items():
            self.kvfile.write('%s: %s%s' % (k, v, linesep))
        else:
            self.kvfile.close()
