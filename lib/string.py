def center(s, width, fillchar=' '):
    return s.center(int(width), fillchar)

def repeat(s, n):
    return s * int(n)

def replace(s, old, new, count=-1):
    return s.replace(old, new, int(count))
