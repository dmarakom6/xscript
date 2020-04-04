#!/usr/bin/python3

import os
import shlex
import string
import time
import xscript

class XscriptInterpreter():

    def __init__(self, string='', debug=False, var={}, itervar={}):
        self.restart(string, debug, var, itervar)

    def delete(self, *names):
        for name in names:
           del self.var[name]

    def exit(self, code=0):
        exit(int(code))

    def end_flag(self, flag):
        if len(self.block) == 0:
            raise TypeError('Flag not find: %s' % flag)
        elif self.block[-1] == flag:
            for line in self.program[self.now::-1]:
                line = line.lstrip()
                if self.debug:
                    print('end-', line)
                if line.startswith(flag):
                    self.now -= 1
                    del self.block[-1]
                    return
                else:
                    self.now -= 1
        else:
            raise TypeError('Flag not find: %s' % flag)

    def for_flag(self, name, fromnum, tonum, stepnum=None):
        if name[0] not in string.ascii_letters + string.digits + '_':
            raise TypeError('Invalid name: %s' % name)
        else:
            for char in name:
                if char not in string.ascii_letters + '_':
                    raise TypeError('Invalid name: %s' % name)
            else:
                nextvar = None
                if name not in self.itervar:
                    if stepnum == None:
                        fromnum = int(self.replacevar(fromnum))
                        tonum = int(self.replacevar(tonum))
                        stepnum = 1
                    else:
                        fromnum = int(self.replacevar(fromnum))
                        tonum = int(self.replacevar(tonum))
                        stepnum = int(self.replacevar(stepnum))
                    self.itervar[name] = iter(range(fromnum, tonum, stepnum))
                    nextvar = next(self.itervar[name], None)
                    if self.debug:
                        print('for<', nextvar)
                    if nextvar != None:
                        self.block.append('for')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        for line in self.program[self.now:]:
                            line = line.lstrip()
                            if self.debug:
                                print('for-', line)
                            if line == 'end for':
                                return
                            else:
                                self.now += 1
                        else:
                            raise TypeError('Loop without end')
                else:
                    nextvar = next(self.itervar[name], None)
                    if self.debug:
                        print('for<', nextvar)
                    if nextvar != None:
                        self.block.append('for')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        for line in self.program[self.now:]:
                            line = line.lstrip()
                            if self.debug:
                                print('for-', line)
                            if line == 'end for':
                                return
                            else:
                                self.now += 1
                        else:
                            raise TypeError('Loop without end')

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
    
    def restart(self, string='', debug=False, var={}, itervar={}):
        self.string = string.replace(os.sep, '\n')
        self.program = self.string.split('\n')
        self.debug = debug
        self.var = var
        self.itervar = itervar

    def run(self):
        self.now = 0
        self.block = []
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now].lstrip()
            else:
                self.exit()
                break
            lines = shlex.split(line)
            ret = None
            if self.debug:
                print(self.now, 'run>', lines)
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
                    raise TypeError('error Unknow command: %s' % lines[0])
            except Exception as err:
                print('Traceback:')
                print('line', self.now + 1)
                print('-> ', line)
                print('Error: %s' % str(err))
                self.exit(1)
                break
            else:
                self.now += 1

    def puts(self, *args):
        for item in args:
            print(self.replacevar(item))

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
let start := [xscript.time.time]
xscript.turtle.color red yellow
xscript.turtle.begin_fill
xscript.turtle.speed 15
for i 0 360
    xscript.turtle.forward 1
    xscript.turtle.left 1
end for
xscript.turtle.end_fill
let end := [xscript.time.time]
let end -= $start
puts $end
'''
ipr = XscriptInterpreter(code, True)
ipr.run()
