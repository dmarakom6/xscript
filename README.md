# xscript
A tiny language

Don't imitate this, It's too easy!!!

I don't like to add comments, so would you help me?

# How does it work?
[Click here!](howto.md)

# How fast is it?
Like lightning! No, no, it's a lie. Just a bit slow.

We use a little program to calculate it, you can find it in `script/circle.xs`.

The python version is like this:
  ```python
  import turtle
  import time
  
  turtle.color('red', 'yellow')
  turtle.begin_fill()
  turtle.speed(15)
  for i in range(0, 360, 1):
      turtle.forward(1)
      turtle.left(1)
  turtle.end_fill()
  ```
The result is:
| language | average   |
| -------- | --------- |
| python   | 10.29742s |
| xscript  | 10.90012s |

Also, you can read ```debug.txt``` for debug detail.
> It's too long, I suggest you don't read it!
