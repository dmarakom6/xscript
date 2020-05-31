# xscript/core.py
# xscript core

import lib
import os
from prettytable import PrettyTable
try:
    import readline
except:
    print("xscript: No 'readline'")
import shlex
import string
import textwrap


class XScriptInterpreter(object):
    # xscript interpreter core
    def __init__(self, string='', var={}, argv=[]):
        self.restart(string, var, argv)

    def debug(self):
        # debug
        try:
            print('start debug'.center(os.get_terminal_size()[0], '='))
        except:
            print('xscript: start debug')
        cmd = ''
        while cmd != 'exit':
            cmd = input('debug> ')
            if cmd == '':
                pass
            elif cmd == 'exit':
                pass
            elif cmd == 'now':
                print('.'.join(self.block))
            elif cmd.startswith('show '):
                if cmd[5:] in self.var:
                    table = PrettyTable(['name', 'value', 'type'])
                    name = cmd[5:]
                    value = self.var[name]
                    if len(str(value)) >= 50:
                        table.add_row([name, textwrap.shorten(str(value), 50, placeholder='...'), str(type(value))[8:-2]])
                    else:
                        table.add_row([name, str(value), str(type(value))[8:-2]])
                    print(table)
                else:
                    print("ERROR: name '%s' is not defined" % cmd[5:])
            elif cmd == 'vars':
                table = PrettyTable(['name', 'value', 'type'])
                for k, v in self.var.items():
                    if len(str(v)) >= 50:
                        table.add_row([k, textwrap.shorten(str(v), 50, placeholder='...'), str(type(v))[8:-2]])
                    else:
                        table.add_row([k, str(v), str(type(v))[8:-2]])
                else:
                    print(table)
            else:
                print("ERROR: No debug command: '%s'" % cmd)
        else:
            try:
                print('end debug'.center(os.get_terminal_size()[0], '='))
            except:
                print('xscript: end debug')

    def delete(self, *names):
	# delete the name in self.var
        for name in names:
            if name not in self.const:
                del self.var[name]
            else:
                raise TypeError('%s is a const variable.' % name)

    def exit(self, code=0):
	# raise exit code and exit
        exit(int(code))

    def end_flag(self, flag):
	# end is a flag, not function, it's very complex
	# BUG: on flag nesting like double for
        if len(self.block) == 0:
            raise TypeError('Flag not find: %s' % flag)
        elif self.block[-1] == flag:
            inblock = 0
            for line in self.program[self.now::-1]:
                line = line.lstrip()
                if line == 'end ' + flag:
                    inblock += 1
                if line.startswith(flag + ' '):
                    if inblock == 0:
                        self.now -= 1
                        del self.block[-1]
                        return
                    else:
                        inblock -= 1
                else:
                    self.now -= 1
        else:
            raise TypeError('Flag not find: %s' % flag)

    def for_flag(self, name, fromnum, tonum, stepnum=None):
	# for is a flag, not function, it's more complex than end_flag
	# for use built-in function iter() to start a loop
        if name[0] not in string.ascii_letters + string.digits + '_':
            raise TypeError('Invalid name: %s' % name)
        else:
            for char in name[1:]:
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
                    if nextvar != None:
                        self.block.append('for')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        infor = 0
                        for line in self.program[self.now - 1:]:
                            self.now += 1
                            line = line.lstrip()
                            if line.startswith('for '):
                                infor += 1
                            if line == 'end for':
                                if infor == 0:
                                    return
                                else:
                                    infor -= 1
                            else:
                                pass
                        else:
                            raise TypeError('Loop without end')
                else:
                    nextvar = next(self.itervar[name], None)
                    if nextvar != None:
                        self.block.append('for')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        infor = 0
                        for line in self.program[self.now - 1:]:
                            self.now += 1
                            line = line.lstrip()
                            if line.startswith('for '):
                                infor += 1
                            elif line == 'end for':
                                if infor == 0:
                                    return
                                else:
                                    infor -= 1
                            else:
                                pass
                        else:
                            raise TypeError('Loop without end')

    def foreach_flag(self, name, iterator):
	# foreach is a flag, not function, it's easier than for
        if name[0] not in string.ascii_letters + string.digits + '_':
            raise TypeError('Invalid name: %s' % name)
        else:
            for char in name[1:]:
                if char not in string.ascii_letters + '_':
                    raise TypeError('Invalid name: %s' % name)
            else:
                nextvar = None
                if name not in self.itervar:
                    self.itervar[name] = iter(self.replacevar(iterator))
                    nextvar = next(self.itervar[name])
                    if nextvar != None:
                        self.block.append('foreach')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        inforeach = 0
                        for line in self.program[self.now - 1:]:
                            self.now += 1
                            line = line.lstrip()
                            if line.startswitch('foreach '):
                                inforeach += 1
                            elif line == 'end foreach':
                                if inforeach == 0:
                                    return
                                else:
                                    inforeach -= 1
                            else:
                                pass
                        else:
                            raise TypeError('Loop without end')
                else:
                    nextvar = next(self.itervar[name], None)
                    if nextvar != None:
                        self.block.append('foreach')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        inforeach = 0
                        for line in self.program[self.now - 1:]:
                            self.now += 1
                            line = line.lstrip()
                            if line.startswitch('foreach '):
                                inforeach += 1
                            elif line == 'end foreach':
                                if inforeach == 0:
                                    return
                                else:
                                    inforeach -= 1
                            else:
                                pass
                        else:
                            raise TypeError('Loop without end')

    def gets(self, prompt='?'):
	# gets is very easy, read it!
        return input(prompt)

    def let(self, name, symbol, value):
        # let is just a assignment statement, it support 10 operators.
        if self.testname(name):
            if name not in self.var and symbol not in ['=', '#=', '.=']:
                raise TypeError("Undefined name cannot use '%s'" % symbol)
            value = self.replacevar(value)
            if symbol == '=':
                self.var[name] = value
            elif symbol == '#=':
                self.var[name] = int(value)
            elif symbol == '.=':
                self.var[name] = float(value)
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
        else:
            raise TypeError("Invalid name: '%s'"% name)

    def puts(self, *args):
	# puts just print something to the console
        for item in args:
            print(self.replacevar(item), end=' ')
        else:
            print()

    def replacefunction(self, s):
        # you cannot call it in your script
        # you just can call 2 functions in []
        exp = []
        for item in shlex.split(s):
            if item[0] == '&':
                exp.append(self.var[item[1:]])
            elif item[0] == '$':
                exp.append(str(self.var[item[1:]]))
            elif item[0] == '#':
                try:
                    exp.append(int(self.var[item[1:]]))
                except:
                    exp.append(None)
            elif item[0] == '.':
                try:
                    exp.append(float(self.var[item[1:]]))
                except:
                    exp.append(None)
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
	# you cannot call it in your script
	# it just replace name of variable to its value
        if value[0] == '[' and value[-1] == ']':
            return self.replacefunction(value[1:-1])
        elif value[0] == '&':
            return self.var[value[1:]]
        elif value[0] == '$':
            return str(self.var[value[1:]])
        elif value[0] == '#':
            try:
                return int(self.var[value[1:]])
            except:
                return None
        elif value[0] == '.':
            try:
                return float(self.var[value[1:]])
            except:
                return None
        else:
            return value
    
    def restart(self, string='', var={}, argv=[]):
        # you cannot call it in your script
        # it just set some global variable like variable
        self.program = string
        self.var = var
        self.itervar = {}
        self.var['true'] = True
        self.var['false'] = False
        self.var['null'] = None
        self.var['argv']= argv
        self.var['version'] = 0.0
        self.const = ['true', 'false', 'null', 'argv', 'version']

    def run(self):
        # run is a very import function, you understand
        self.now = 0
        self.block = []
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now].lstrip()
            else:
                self.exit()
                break
            lines = shlex.split(line)
            try:
                if lines == []:
                        pass
                elif lines[0][0] == '#':
                    pass
                elif lines[0] == 'debug':
                    self.debug(*lines[1:])
                elif lines[0] == 'delete':
                    self.delete(*lines[1:])
                elif lines[0] == 'end':
                    self.end_flag(*lines[1:])
                elif lines[0] == 'exit':
                    self.exit(*lines[1:])
                elif lines[0] == 'for':
                    self.for_flag(*lines[1:])
                elif lines[0] == 'foreach':
                    self.foreach_flag(*lines[1:])
                elif lines[0] == 'gets':
                    self.gets(*lines[1:])
                elif lines[0] == 'let':
                    self.let(*lines[1:])
                elif lines[0] == 'puts':
                    self.puts(*lines[1:])
                elif lines[0] == 'while':
                    self.while_flag(*lines[1:])
                elif lines[0][:8] == 'xscript.':
                    self.xscript(*lines)
                else:
                    raise TypeError('Unknow command: %s' % lines[0])
            except Exception as err:
                print('Traceback:')
                print('line', self.now + 1)
                print('-> ', line)
                print('Error: %s' % str(err))
                self.exit(1)
                break
            else:
                self.now += 1

    def testname(self, name):
        if name[0] not in string.ascii_letters + '_':
            return False
        else:
            for char in name[1:]:
                if char not in string.ascii_letters  + string.digits + '_':
                    return False
            else:
                if name in self.const:
                    return False
                else:
                    return True

    def while_flag(self, left, symbol, right):
        # while is a flag, not function
        left = self.replacevar(left)
        right = self.replacevar(right)
        if symbol == '=':
            relation = (left == right)
        elif symbol == '!=':
            relation = (left != right)
        elif symbol == '>':
            relation = (left > right)
        elif symbol == '>=':
            relation = (left >= right)
        elif symbol == '<':
            relation = (left < right)
        elif symbol == '<=':
            relation = (left <= right)
        else:
            raise TypeError('Unsupported operate: %s' % symbol)
        if relation:
            self.block.append('while')
        else:
            inwhile = 0
            for line in self.program[self.now - 1:]:
                self.now += 1
                line = line.lstrip()
                if line.startswith('while '):
                    inwhile += 1
                elif line == 'end while':
                    inwhile -= 1
                else:
                    pass
            else:
                raise TypeError('Loop without end')

    def xscript(self, path, *args):
        # xscript is an important function that it can call outer function
        arg = []
        for item in args:
            arg.append(self.replacevar(item))
        else:
            path = path.split('.')
            obj = lib
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    raise TypeError('No attribute: %s' % item)
            else:
                if type(obj) == type(lambda x: x):
                    # >>> type(abs)
                    # <class 'builtin_function_or_method'>
                    # >>> type(lambda: 1)
                    # <class 'function'>
                    # >>> type(abs) == type(lambda: 1)
                    # False
                    # >>> # so we use `type(obj) == type(lambda x: x)` to compare function and variable
                    return obj(*arg)
                elif len(arg) == 0:
                    return obj
                else:
                    raise TypeError("'%s' is not callable" % path)

