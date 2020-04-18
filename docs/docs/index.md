# xscript
xscript是一个使用python编写的微型语言. 其源代码(`core.py`)绝对不会超过1000行.

> 有一部分原因是我将大部分的内容都写进了xscript库(`xscript/xscript`)

> 这门语言是设计为嵌入到一个软件里的, 当然是越小巧越好了!

# 如何运行我的代码?
你可以在xscript目录下, 在终端中输入`xscript.py [你的文件]`就可以运行了.

## 如何调试我的代码?
很抱歉, 解释器有简单的调试功能(主要是开发期间), 但并没有命令行选项来打开调试功能.

但, 请打开`xscript.py`, 将第19行改为:
```python
interpreter = core.XScriptInterpreter(source, debug=True)
```
你自己也可以重写这个文件以添加debug功能.

# xscript有多快?
我迄今为止只做了一个测试,取平均值得知, 运行差不多(将xscript翻译成python)的代码,
比xscript比python慢了一点(大约零点几秒).

# 更多
我特地写了一个[文档](howto.md)来解释其工作原理.

如果你想更多地了解xscript, 请[点击这里](./learn.md).

xscript有一堆内置函数库, 和python**有点儿**不相同, 你可以[点击这里](lib/index.md)了解标准库.

# 许可证
该程序使用GNU通用许可证第3版(GPLv3).

你可以任意复制之.
