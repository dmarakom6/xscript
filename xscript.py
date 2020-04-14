#!/usr/bin/python3

import core
import os.path as path
import sys

def main():
    if not path.isfile(sys.argv[1]):
        print('Error: No such file or directory: %s' % sys.argv[1])
        exit(1)
    else:
        source = open(sys.argv[1], 'r+').read()
        interpreter = core.XScriptInterpreter(source, argv=sys.argv[1:],debug=False)
        interpreter.run()

if __name__ == '__main__':
    # main()
    source = open(sys.argv[1], 'r+').read()
    interpreter = core.XScriptInterpreter(source, argv=sys.argv[1:],debug=False)
    interpreter.run()
