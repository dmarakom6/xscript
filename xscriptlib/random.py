import random as _random

def choice(*seq):
    return _random.choice(seq)

def rand():
    return _random.random()

def randint(a, b):
    return _random.randint(a, b)

def uniform(a, b):
    return _random.uniform(a, b)
