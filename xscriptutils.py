# xscript/xscriptutils.py
# xscript utils

class Arguments(object):

    def __init__(self, args):
        self._args = args

    def get(self, name):
        if name in aself._args:
            return self._args[name]
        else:
            return None

    def length(self):
        return len(self._args)

