#!/usr/bin/python3

import os
import shlex
import string
import time
import xscript

class XscriptInterpreter():
    
    def __init__(self, string='', var={}):
        self.restart(string, var)

    def delete(self, *names):
        for name in names:
           del self.var[name]

    def exit(self, code=0):
        print('\nProgram raise exit code: %s' % code)
        exit(code)

    def gets(self, prompt=''):
        return input(prompt)

    def let(self, name, symbol, value):
        if name[0] not in string.ascii_letters + string.digits + '_':
            raise TypeError('Invalid name: %s' % name)
        else:
            for char in name:
                if char not in string.ascii_letters + '_':
                    raise TypeError('Invalid name: %s' % name)
            else:
                if name not in self.var and symbol == ':=':
                    self.var[name] = value
                elif name not in self.var and symbol != ':=':
                    raise TypeError('Undefined name cannot use other operate')
                elif symbol == '=':
                    self.var[name] = value
                elif symbol == '+=':
                    self.var[name] += value
                elif symbol == '-=':
                    self.var[name] -= value
                elif symbol == '*=':
                    self.var[name] *= value
                elif symbol == '/=':
                    self.var[name] /= value
                elif symbol == '**=':
                    self.var[name] **= value
                elif symbol == '>>=':
                    self.var[name] >>= value
                elif symbol == '<<=':
                    self.var[name] <<= value
                else:
                    raise TypeError('Unsupported operate: %s' % symbol)

    def restart(self, string='', var={}):
        self.string = string.replace(os.sep, '\n')
        self.program = self.string.split('\n')
        self.var = var

    def run(self):
        self.now = 1
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now - 1]
            else:
                self.exit()
                break
            lines = shlex.split(line)
            ret = None
            try:
                if lines == []:
                    pass
                elif lines[0][0] == '#':
                    pass
                elif lines[0] == 'delete':
                    self.delete(*lines[1:])
                elif lines[0] == 'exit':
                    self.exit(*lines[1:])
                    break
                elif lines[0] == 'gets':
                    self.gets(*lines[1:])
                elif lines[0] == 'let':
                    self.let(*lines[1:])
                elif lines[0] == 'puts':
                    self.puts(*lines[1:])
                elif lines[0][:8] == 'xscript.':
                    self.xscript(*lines)
                else:
                    ret = 'error Unknow command: %s' % lines[0]
            except Exception as err:
                print('Traceback:')
                print('line', self.now)
                print('-> ', line)
                print('Error: %s' % str(err))
                self.exit(1)
                break
            else:
                self.now += 1

    def puts(self, *args):
        for item in args:
            print(item)

    def xscript(self, path, *args):
        path = path.split('.')
        obj = xscript
        for item in path[1:]:
            if hasattr(obj, item):
                obj = getattr(obj, item)
            else:
                raise TypeError('No attribute: %s' % item)
        else:
            return obj(*args)

code = '''
puts Hell
'''
ipr = XscriptInterpreter(code)
ipr.run()
