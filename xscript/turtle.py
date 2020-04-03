# xscript/turtle.py

import turtle as _turtle

def back(n):
    _turtle.back(int(n))

def begin_fill():
    _turtle.begin_fill()

def circle(radius, extent=None, steps=None):
    radius = float(radius)
    if extent:
        extent = float(extent)
    if steps:
        steps = int(steps)
    _turtle.circle(radius, extent, steps)

def clear():
    _turtle.clear()

def clearstamp(n):
    _turtle.clearstamp(int(n))

def clearstamps(n=None):
    if n:
        n = int(n)
    _turtle.clearstamps(n)

def color(color1, color2):
    _turtle.color(color1, color2)

def down():
    _turtle.down()

def end_fill():
    _turtle.end_fill()

def forward(n):
    _turtle.forward(int(n))

def goto(x, y=None):
    if not y:
        _turtle.goto(int(x))
    else:
        _turtle.goto(int(x), int(y))

def hide():
    _turtle.hideturtle()

def home():
    _turtle.home()

def left(n):
    _turtle.left(int(n))

def mainloop():
    _turtle.mainloop()

def reset():
    _turtle.reset()

def right(n):
    turtle.right(int(n))

def show():
    _turtle.showturtle()

def stamp():
    return _turtle.stamp()

def speed(speed=None):
    if speed:
        speed = int(speed)
    _turtle.speed(speed)

def undo():
    _turtle.undo()

def up():
    _turtle.up()

def write(s):
    _turtle.write(s)
