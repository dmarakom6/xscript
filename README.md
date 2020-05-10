> I'm so sorry about delete the English version README.

# 什么是xscript?
xscript是用python编写的一个非常小巧的编程语言, 它的核心(`core.py`)不会超过1000行(到现在为止还没有到400行).

没有函数, 没有判断结构. 它只有最基本的变量管理, 所有类型的循环结构, 可调用的外部函数(python), 没了!
> xscript的核心可以缩减很小, 因为所有主要的功能都在库`xscript`中.

> 你可以使用 `import xscript` 来导入该库, 函数定义和用法都和python差不多.

> 这门语言是设计为嵌入式的, 这样也可以保证安全.

> `core.py`中的核心(XScriptInterpreter)非常清晰, 每个函数对应一个功能.

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入 `xscript.py [你的文件名]` 来运行.

当然, 你可以看看`xscript/xscript`目录下的例子.

## 如何调试我的代码?
请在你的代码中加入`debug`, 并且保持`XScriptInterpreter`中的debug为`True`

# 它有多快?
就像闪电一样快!!

不对, 不对, 这绝对不可能.只比python慢了一点.
> 你当然可以直接试一试!
