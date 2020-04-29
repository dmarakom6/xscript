def Bool(n):
  if n == 'True':
    return True
  elif n == 'False':
    return False
  elif n:
    return True
  else:
    return False

def Complex(n):
  return complex(n)

def Float(n):
  return float(n)

def Int(n):
  return int(n)

def List(*item):
  return list(item)
