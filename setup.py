# xscript/setup.py

from distutils.core import setup
from time import strftime

setup(
    name='xscript',
    version=strftime('%Y-%m-%d'),
    license='GPLv3',
    packages=['xscriptlib'],
    py_modules=['xscriptcore']
)
