# xscript文档
> 这里是xscript0.0的文档

## 什么是xscript?
xscript是用python编写的一个非常小巧的编程语言, 它的核心(`core.py`)不会超过1000行.

没有函数, 没有判断结构. 它只有最基本的变量管理, 所有类型的循环结构, 可调用的外部函数(python实现), 没了!
> xscript的核心可以缩减很小, 因为所有主要的功能都在库`lib`中

> 你可以使用 `import lib` 来导入该库, 函数定义和用法都和python差不多

> 这门语言是设计为嵌入式的, 这样也可以保证安全以及运行时的效果

## 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`xscript.py [FILE]`来运行.

当然, 你可以看看`xscript/script`目录下的例子.

## 如何调试我的代码?
在`2020-5-10`次提交中更新了debug的用法.

现在允许你与debug交互.

## 它有多快?
求xscript运行时有多快是一件麻烦的事情, 我们不高兴做这些没有意义的事情.
> 经过对比: python比xscript快了一秒左右(`script/circle.xs`)

## 学习, 改进xscript
xscript是一门开源编程语言, 它现在还处于开发阶段, 希望你能帮助改进xscript.

- [报告一个BUG](bug.md)
- [学习xscript](learn/index.md)
- [xscript如何工作](howto.md)

- - -

非常抱歉, xscript文档是简体中文版的, 请大家谅解. 你可以使用Google Chrome的翻译功能来阅读文档.

xscript文档的多语种版本是有帮助的, 希望您能够将该文档翻译成相应的语言.
