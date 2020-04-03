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
        exit(int(code))

    def end_flag(self, flag):
        if len(self.block) == 0:
            raise TypeError('Flag not find: %s' % flag)
        elif self.block[-1] == flag:
            pass
        else:
            raise TypeError('Flag not find: %s' % flag)

    def for_flag(name, fromnum, tonum, stepnum=None):
         if name[0] not in string.ascii_letters + string.digits + '_':
            raise TypeError('Invalid name: %s' % name)
        else:
            for char in name:
                if char not in string.ascii_letters + '_':
                    raise TypeError('Invalid name: %s' % name)
            else:
                if stepnum == None:
                    fromnum = int(selfreplacevar(fromnum))
                    tonum = int(self.replacevar(tonum))
                    stepnum = 1
                else:
                    stepnum = int(self.replacevar(stepnum))
                self.itervar[name] = iter(range(fromnum, tonum, stepnum))
                try:
                    self.var[name] = next(self.itervar[name])
                except:
                    pass
                else:
                    pass

    def gets(self, prompt=''):
        return input(prompt)

    def let(self, name, symbol, value):
        value = self.replacevar(value)
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
                    raise TypeError("Undefined name just can use ':='")
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

    def replacefunction(self, s):
        exp = []
        for item in shlex.split(s):
            if item[0] == '$':
                exp.append(self.var[item[1:]])
            else:
                exp.append(item)
        else:
            print('>>', exp)
            if exp[0] == 'gets':
                return self.gets(*exp[1:])
            elif exp[0][:8] == 'xscript.':
                return self.xscript(*exp)
            else:
                raise TypeError('Unknow replace function command : %s' % ret[0])

    def replacevar(self, value):
        if value[0] == '[' and value[-1] == ']':
            return self.replacefunction(value[1:-1])
        elif value[0] == '$':
            return self.var[value[1:]]
        else:
            return value
    
    def restart(self, string='', var={}):
        self.string = string.replace(os.sep, '\n')
        self.program = self.string.split('\n')
        self.var = var

    def run(self):
        self.now = 1
        self.block = []
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now - 1].lstrip()
            else:
                self.exit()
                break
            lines = shlex.split(line)
            ret = None
            print('>', lines)
            try:
                if lines == []:
                    pass
                elif lines[0][0] == '#':
                    pass
                elif lines[0] == 'delete':
                    self.delete(*lines[1:])
                elif lines[0] == 'end':
                    self.end_flag(*lines[1:])
                elif lines[0] == 'exit':
                    self.exit(*lines[1:])
                elif lines[0] == 'for':
                    self.for_flag(*lines[1:])
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
            if item[0] == '$':
                print(self.var[item[1:]], end='')
            elif item[0] == '[' and item[-1] == ']':
                print(self.replacefunction(item[1:-1]), end='')
            else:
                print(item)

    def xscript(self, path, *args):
        arg = []
        for item in args:
            arg.append(self.replacevar(item))
        else:
            path = path.split('.')
            obj = xscript
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    raise TypeError('No attribute: %s' % item)
            else:
                return obj(*arg)

code = '''
let a := 50
let b := 60
xscript.turtle.color red yellow
xscript.turtle.begin_fill
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.stamp
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.stamp
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.stamp
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.stamp
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.stamp
xscript.turtle.forward $a
xscript.turtle.left $b
xscript.turtle.end_fill
xscript.turtle.mainloop
exit 1
'''
ipr = XscriptInterpreter(code)
ipr.run()
