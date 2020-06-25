# xscript/setup.py

from distutils.core import setup
from time import strftime

setup(
    name='xscript',
    #version=strftime('%Y-%m-%d'),
    version='0.5',
    license='GPLv3',
    description='xscript programming language',
    url='https://github.com/jason-bowen-zheng/xscript',
    packages=['xscriptlib'],
    py_modules=['xscriptcore'],
)
