#!/usr/bin/python3
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import core
import os.path as path
import sys

def main():
    if len(sys.argv) < 2:
        print('xscript: Not enough argument')
        exit(1)
    elif not path.isfile(sys.argv[1]):
        print('xscript: No such file or directory: %s' % sys.argv[1])
        exit(1)
    else:
        source = open(sys.argv[1], 'r+').readlines()
        interpreter = core.XScriptInterpreter(source, argv=sys.argv[1:])
        interpreter.run()

if __name__ == '__main__':
    main()
