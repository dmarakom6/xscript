import os
import shlex
import string
import xscript


class XScriptInterpreter():

    def __init__(self, string='', debug=False, var={}, itervar={}, argv=[]):
        self.restart(string, debug, var, itervar, argv)

    def delete(self, *names):
        for name in names:
            if name not in self.const:
                del self.var[name]
            else:
                raise TypeError('%s is a const variable.' % name)

    def exit(self, code=0):
        exit(int(code))

    def end_flag(self, flag):
        if len(self.block) == 0:
            raise TypeError('Flag not find: %s' % flag)
        elif self.block[-1] == flag:
            inblock = 0
            for line in self.program[self.now::-1]:
                line = line.lstrip()
                if self.debug:
                    print('end-', line)
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
                    if self.debug:
                        print('for<', nextvar)
                    if nextvar != None:
                        self.block.append('for')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        infor = 0
                        for line in self.program[self.now + 1:]:
                            line = line.lstrip()
                            if self.debug:
                                print('for-', line)
                            if line.startswith('for '):
                                infor += 1
                            if line == 'end for':
                                if infor == 0:
                                    self.now += 1
                                    return
                                else:
                                    infor -= 1
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
                        infor = 0
                        for line in self.program[self.now + 1:]:
                            line = line.lstrip()
                            if self.debug:
                                print('for-', line)
                            if line.startswith('for '):
                                infor += 1
                            if line == 'end for':
                                if infor == 0:
                                    self.now += 1
                                    return
                                else:
                                    infor -= 1
                            else:
                                self.now += 1
                        else:
                            raise TypeError('Loop without end')

    def foreach_flag(self, name, iterator):
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
                    if self.debug:
                        print('foreach<', nextvar)
                    if nextvar != None:
                        self.block.append('foreach')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        inforeach = 0
                        for line in self.program[self.now + 1:]:
                            line = line.lstrip()
                            if self.debug:
                                print('foreach-', line)
                            if line.startswitch('foreach '):
                                inforeach += 1
                            if line == 'end foreach':
                                if inforeach == 0:
                                    self.now += 1
                                    return
                                else:
                                    inforeach -= 1
                            else:
                                self.now += 1
                        else:
                            raise TypeError('Loop without end')
                else:
                    nextvar = next(self.itervar[name], None)
                    if self.debug:
                        print('forach<', nextvar)
                    if nextvar != None:
                        self.block.append('foreach')
                        self.var[name] = nextvar
                    else:
                        del self.itervar[name]
                        inforeach = 0
                        for line in self.program[self.now:]:
                            line = line.lstrip()
                            if self.debug:
                                print('foreach-', line)
                            if line.startswitch('foreach '):
                                inforeach += 1
                            if line == 'end foreach':
                                if inforeach == 0:
                                    self.now += 1
                                    return
                                else:
                                    inforeach -= 1
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
            for char in name[1:]:
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

    def puts(self, *args):
        for item in args:
            print(self.replacevar(item), end=' ')
        else:
            print()

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
    
    def restart(self, string='', debug=False, var={}, itervar={}, argv=[]):
        self.string = string.replace(os.sep, '\n')
        self.program = self.string.split('\n')
        self.debug = debug
        self.var = var
        self.var['TRUE$'] = True
        self.var['FALSE$'] = False
        self.var['NULL$'] = None
        self.var['ARGV$']= argv
        self.const = ['TRUE$', 'FALSE$', 'ARGV$', 'NULL$']
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
            
    def while_flag(self, left, symbol, right):
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
            for line in self.program[self.now + 1:]:
                line = line.lstrip()
                if self.debug:
                    print('while-', self.now, line)
                if line.startswith('while '):
                    inwhile += 1
                if line == 'end while':
                    if inwhile == 0:
                        self.now += 1
                        return
                    else:
                        inwhile -= 1
                else:
                    self.now += 1
            else:
                raise TypeError('Loop without end')

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
                if type(obj) == type(lambda x: x):
                    return obj(*arg)
                elif len(arg) == 0:
                    return obj
                else:
                    raise TypeError("'%s' is not callable" % path)
