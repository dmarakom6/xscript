> I'm so sorry about delete the English version README.

# 什么是xscript?
xscript是用python编写的一个非常小巧的编程语言, 它的核心(`core.py`)不会超过1000行(到现在为止还没有到400行).
> 所以xscript的核心可以缩减很小, 所有主要的功能都在库`xscript`中.
> 你可以使用 `import xscript` 来导入该库, 函数定义和用法都和python差不多.

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入 `xscript.py [你的文件名]` 来运行.

当然, 你可以看看`xscript/xscript`目录下的例子.

## 如何调试我的代码?
很遗憾, 源代码中并没有关于`-debug`开关的处理, 你可以把`xscript.py`的第19行改为:
```python
interpreter = core.XScriptInterpreter(source, debug=True)
```

当然, 你也可以改写该文件添加一个debug开关.

# 它有多快?
就像闪电一样快!!

不对, 不对, 这绝对不可能.只比python慢了一点.