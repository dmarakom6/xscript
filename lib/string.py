# xscript/lib/string.py

def left(s, n):
  return s[int(n):]

def mid(s, m, n):
  return s[int(m): int(n)]

def right(s, n):
  return s[:int(n)]
