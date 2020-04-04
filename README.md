# xscript
A tiny language

# How fast is it?
We use a little program to calculate it, you can find it in ```xscript.py```.

The python version is like this:
  ```python
  import turtle
  import time
  
  start = time.time()
  turtle.color('red', 'yellow')
  turtle.begin_fill()
  turtle.speed(15)
  for i in range(0, 360, 1):
      turtle.forward(1)
      turtle.left(1)
  turtle.end_fill()
  print(time.time() - start)
  ```
The result is:
| language | average   |
| -------- | --------- |
| python   | 10.29742s |
| xscript  | 10.90012s |
Also, you can read ```debug.txt``` for debug detail.
