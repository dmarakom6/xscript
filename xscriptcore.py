# xscript/xscriptcore.py
# xscript core

import colorama as color
import os
from prettytable import PrettyTable
import re
try:
    import readline
except:
    print("xscript: init: warning: No 'readline' modules")
import shlex
import string
import sys
import textwrap
import time


class XScriptInterpreter(object):
    def __init__(self, string='', var={}, argv=[]):
        # see restart
        self.restart(string, var, argv)

    def addr(self, name):
        try:
            return id(self.var[name])
        except:
            return 0

    def assert_(self, left, symbol, right):
        relation = self.compare(left, symbol, right)
        if relation:
            pass
        else:
            if self.profile.get('assert-raise-err') == 'true':
                raise TypeError('Assertion')
            else:
                print('xscript: %d: warning: Assertion' % self.now)

    def call(self, path, *args):
        if self.isfunction(path):
            pass
        else:
            arg = []
            for item in args:
                arg.append(self.replacevar(item))
            path = path.split('.')
            obj = self.var[path[0]]
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    raise TypeError("No attribute '%s'" % item)
            else:
                if callable(obj):
                    # function and method
                    return obj(*arg)
                else:
                    if len(args) != 0:
                        raise TypeError("'%s' is not callable" % '.'.join(path))
                    else:
                        return obj

    def color(self, action, *args):
        if action == 'init':
            arg = {}
            for item in args:
                arg[item] = True
            else:
                color.init(**arg)
        elif action == 'reset':
            if len(args) != 0:
                raise TypeError('reset takes no argument but %d gave' % len(args))
            else:
                print(color.Style.RESET_ALL, end='')
        elif action == 'setback':
            if len(args) != 1:
                raise TypeError('setback takes 1 argument but %d gave' % len(args))
            else:
                if getattr(color.Back, args[0]):
                    print(getattr(color.Back, args[0]), end='')
                else:
                    raise TypeError("No back color '%s'" % args[1])
        elif action == 'setfore':
            if len(args) != 1:
                raise TypeError('setfore takes 1 argument but %d gave' % len(args))
            else:
                if getattr(color.Fore, args[0]):
                    print(getattr(color.Fore, args[0]), end='')
                else:
                    raise TypeError("No fore color '%s'" % args[1])
        elif action == 'setstyle':
            if len(args) != 1:
                raise TypeError('setstyle takes 1 argument but %d gave' % len(args))
            else:
                if getattr(color.Style, args[0]):
                    print(getattr(color.Style, args[0]), end='')
                else:
                    raise TypeError("No style '%s'" % args[1])

        else:
            raise TypeError("No subcommand '%s'" % action)

    def debug(self):
        if self.profile.get('debug') != 'true':
            return
        else:
            try:
                print('start debug'.center(os.get_terminal_size()[0], '='))
            except:
                print('xscript: %d: info: start debug' % self.now)
            cmd = ''
            while cmd != 'exit':
                cmd = self.gets('debug> ')
                if cmd == '':
                    pass
                elif cmd == 'copyright':
                    print('xscript %s' % self.var['version'])
                    print('Copyright (c) 2020 jason-bowen-zheng.')
                    print('All Right Reserved.')
                elif cmd == 'exit':
                    pass
                elif cmd == 'now':
                    print('.'.join(self.block))
                elif cmd == 'ls':
                    table = PrettyTable(['name', 'value', 'type', 'addrss'])
                    for k, v in self.var.items():
                        if len(str(v)) >= 50:
                            table.add_row([k, textwrap.shorten(str(v), 50, placeholder='...'), str(type(v))[8:-2], hex(id(v))])
                        else:
                            table.add_row([k, str(v), str(type(v))[8:-2], hex(id(v))])
                    else:
                        print(table)
                elif cmd.startswith('show '):
                    if cmd[5:] in self.var:
                        table = PrettyTable(['name', 'value', 'type', 'address'])
                        name = cmd[5:]
                        value = self.var[name]
                        if len(str(value)) >= 50:
                            table.add_row([name, textwrap.shorten(str(value), 50, placeholder='...'), str(type(value))[8:-2], hex(id(value))])
                        else:
                            table.add_row([name, str(value), str(type(value))[8:-2], hex(id(value))])
                        print(table)
                    else:
                        print("ERROR: name '%s' is not defined" % cmd[5:])
                else:
                    print("ERROR: No debug command: '%s'" % cmd)
            else:
                try:
                    print('end debug'.center(os.get_terminal_size()[0], '='))
                except:
                    print('xscript: %d: info: end debug' % self.now)

    def compare(self, left, symbol, right):
        left = self.replacevar(left)
        right = self.replacevar(right)
        if symbol == '=':
            return (left == right)
        elif symbol == '!=':
            return (left != right)
        elif symbol == '>':
            return (left > right)
        elif symbol == '>=':
            return (left >= right)
        elif symbol == '<':
            return (left < right)
        elif symbol == '<=':
            return (left <= right)
        elif symbol == 'in':
            return (left in right)
        elif symbol == '!in':
            return (left not in right)
        elif symbol == 'is':
            return (left is right)
        elif symbol == '!is':
            return (left is not right)
        else:
            raise TypeError('Unsupported operate: %s' % symbol)

    def delete(self, *names):
        for name in names:
            if self.testname(name) and (name in self.var):
                del self.var[name]
            else:
                raise TypeError("Cannot delete variable: '%s'." % name)

    def end_flag(self, flag):
        if len(self.block) == 0:
            raise TypeError('Flag not find: %s' % flag)
        elif self.block[-1] == flag:
            inblock = 0
            for line in self.program[self.now::-1]:
                line = line.strip()
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

    def environ(self, name):
        try:
            return os.environ[name]
        except:
            return None

    def exit(self, code='0'):
        if self.profile.get('show-run-time') == 'true':
            print('xscript: info: program runs %fs' % (time.time() - self.starttime))
        if self.profile.get('show-exit-num') == 'true':
            print('xscript: info: program raise exit code:', self.replacevar(code))
        sys.exit(self.replacevar(code))

    def for_flag(self, name, fromnum, tonum, stepnum=None):
        if not self.testname(name):
            raise TypeError("Invalid name :'%s'" % name)
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
                    for line in self.program[self.now + 1:]:
                        self.now += 1
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
                    for line in self.program[self.now + 1:]:
                        self.now += 1
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
        if not self.testname(name):
            raise TypeError("Invalid name: '%s'" % name)
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
                        if line.startswith('foreach '):
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
                        if line.startswith('foreach '):
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

    def function(self, name, *args):
        if self.testname(name):
            pass
            for line in self.program[self.now - 1]:
                self.now += 1
                if line == 'end function':
                    return
        else:
            raise TypeError("Invalid name: '%s'" % name)

    def get(self, path):
        if path.find('.') != -1:
            return self.var[path]
        else:
            path = path.split('.')
            obj = self.var[path[0]]
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    raise TypeError("No attribute: '%s'" % item)
            else:
                return obj

    def gets(self, prompt='?'):
        try:
            return input(prompt)
        except:
            print()
            raise TypeError('User interrupt')

    def has(self, path):
        if path.find('.') != -1:
            if path in self.var:
                return True
            else:
                return False
        else:
            path = path.split('.')
            obj = self.var[path[0]]
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    return False
            else:
                return True

    def import_(self, name):
        if self.testname(name):
            try:
                self.var[name] = __import__(name)
            except:
                    raise TypeError("No module named: '%s'" % name)
        elif name.find('.') != -1:
            path = name.split('.')
            if path[0] not in self.var:
                try:
                    obj = __import__(path[0])
                except:
                    raise TypeError("No module named: '%s'" % path[0])
            else:
                obj = self.var[path[0]]
            for item in path[1:]:
                if hasattr(obj, item):
                    obj = getattr(obj, item)
                else:
                    raise TypeError("No attribute: '%s'" % item)
            else:
                if self.testname(path[-1]):
                    self.var[path[-1]] = obj
                else:
                    raise TypeError("Invalid name: '%s'" % path[-1])

    def isfunction(self, name):
        return False

    def let(self, name, symbol, value):
        if self.testname(name) and name.find('.') == -1:
            if name not in self.var and symbol != '=':
                raise TypeError("Undefined name cannot use '%s'" % symbol)
            else:
                value = self.replacevar(value)
                if symbol == '=':
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
        elif self.testname(name) and name.find('.') != -1:
            path = name.split('.')
            if path[0] not in self.var:
                raise TypeError("Name '%s' is not defined" % path[0])
            else:
                obj = self.var[path[0]]
                for item in path[1:]:
                    if hasattr(obj, item):
                        obj = getattr(obj, item)
                    else:
                        raise TypeError("No attribute '%s'" % item)
                else:
                    value = self.replacevar(value)
                    if symbol == '=':
                        obj = value
                    elif symbol == '+=':
                        obj += value
                    elif symbol == '-=':
                        obj -= value
                    elif symbol == '*=':
                        obj *= value
                    elif symbol == '/=':
                        obj /= value
                    elif symbol == '**=':
                        obj **= value
                    elif symbol == '>>=':
                        obj >>= value
                    elif symbol == '<<=':
                        obj <<= value
                    else:
                        raise TypeError('Unsupported operate: %s' % symbol)

        else:
            raise TypeError("Invalid name: '%s'"% name)

    def puts(self, *args):
        for item in args:
            if (item := self.replacevar(item)) != None:
                print(item, end=' ')
            else:
                pass
        else:
            print()

    def replacefunction(self, s):
        split = shlex.split(s)[1:]
        exp = [shlex.split(s)[0]]
        for item in split:
            exp.append(self.replacevar(item))
        else:
            if exp[0] == 'addr':
                return self.addr(*exp[1:])
            elif exp[0] == 'call':
                return self.call(*exp[1:])
            elif exp[0] == 'environ':
                return self.environ(*exp[1:])
            elif exp[0] == 'gets':
                return self.gets(*exp[1:])
            elif exp[0] == 'has':
                return self.has(*exp[1:])
            else:
                raise TypeError('Unknow replace function command : %s' % exp[0])

    def replacevar(self, value):
        if value[0] == '[' and value[-1] == ']':
            return self.replacefunction(value[1:-1])
        elif value[0] == '&':
            if self.has(value[1:]):
                return self.get(value[1:])
            else:
                return None
        elif value[0] == '$':
            if self.has(value[1:]):
                return str(self.get(value[1:]))
            elif re.match(r'^(\+|-)?[0-9]+$', value[1:]) or re.match(r'^(\+|-)?[0-9]*\.[0-9]+$', value[1:]):
                return value[1:]
            else:
                return str()
        elif value[0] == '#':
            try:
                return int(self.get(value[1:]))
            except:
                return int()
        elif value[0] == '.':
            try:
                return float(self.get(value[1:]))
            except:
                return float()
        else:
            if re.match(r'^(\+|-)?[0-9]+$', value):
                return int(value)
            elif re.match(r'^(\+|-)?[0-9]+\.[0-9]*', value):
                return float(value)
            else:
                return value

    def restart(self, program, var={}, argv=[]):
        self.program = program
        self.var = var
        self.now = 0
        self.block = []
        self.itervar = {}
        self.var['true'] = True
        self.var['false'] = False
        self.var['null'] = None
        self.var['arg'] = None 
        self.var['interpreter'] = self
        self.var['x'] = __import__('xscriptlib')
        self.var['platform'] = sys.platform
        # don't edit the following version info
        self.var['version'] = '0.5'
        self.const = ['true', 'false', 'null', 'argv', 'interpreter', 'x', 'platform', 'version']
        try:
            self.profile = KVFile(os.environ.get('HOME') + os.sep + '.xscriptrc')
            self.profile.read()
            self.profile.close()
            self.profile = self.profile.kv
        except:
            if sys.platform.startswith('win'):
                print("xscript: warning: No profile '%HOME%\.xscriptrc' found")
            else:
                print("xscript: warning: No profile '~/.xscriptrc' found")
            self.profile = {}

    def run(self):
        if self.profile.get('show-run-time') == 'true':
            self.starttime = time.time()
        else:
            pass
        while True:
            if self.now + 1 <= len(self.program):
                line = self.program[self.now].strip()
            else:
                self.exit()
                break
            lines = shlex.split(line)
            try:
                if lines == []:
                        pass
                elif lines[0][0] == '#':
                    pass
                elif lines[0] == 'assert':
                    self.assert_(*lines[1:])
                elif lines[0] == 'call':
                    self.call(*lines[1:])
                elif lines[0] == 'color':
                    self.color(*lines[1:])
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
                elif lines[0] == 'function':
                    self.function(*lines[1:])
                elif lines[0] == 'gets':
                    self.gets(*lines[1:])
                elif lines[0] == 'import':
                    self.import_(*lines[1:])
                elif lines[0] == 'let':
                    self.let(*lines[1:])
                elif lines[0] == 'puts':
                    self.puts(*lines[1:])
                elif lines[0] == 'while':
                    self.while_flag(*lines[1:])
                else:
                    raise TypeError('Unknow command: %s' % lines[0])
            except Exception as err:
                if self.profile.get('show-detail-err') == 'true':
                    print('In line', self.now + 1)
                    print('-> ', line)
                    print('Error: %s' % str(err))
                    self.exit('1')
                    break
                else:
                    print('xscript: %d: error: %s' % (self.now + 1, str(err)))
                    self.exit('1')
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
        relation = self.compare(left, symbol, right)
        if relation:
            self.block.append('while')
        else:
            inwhile = 0
            for line in self.program[self.now - 1:]:
                self.now += 1
                if line.startswith('while '):
                    inwhile += 1
                elif line == 'end while':
                    inwhile -= 1
                else:
                    pass
            else:
                raise TypeError('Loop without end')


class KVFile():

    def __init__(self, name):
        self.kvfile = open(name, 'r+')
        self.kv = {}

    def read(self):
        self.kv = {}
        for line in self.kvfile.readlines():
            line = line.strip()
            if line == '':
                pass
            elif line[0] == '#':
                pass
            else:
                k, v = line.split(':', 1)
                k, v = k.strip(), v.strip()
                self.kv[k] = v

    def close(self):
        self.kvfile.close()
