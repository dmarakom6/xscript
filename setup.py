# xscript/setup.py

from distutils.core import setup

setup(
    name='xscript',
    version='2020-6-13',
    license='GPLv3',
    requires=['mkdocs', 'prettytable'],
    packages=['xscriptlib'],
    py_modules=['xscriptcore']
)
