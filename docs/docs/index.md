# xscript文档
> 这里是 xscript 0.5 的文档

## 什么是xscript?
xscript 是用 python 编写的一个非常小巧的编程语言, 它的核心(`xscriptcore.py`)很小.
> xscript 的核心可以缩减很小, 因为所有主要的功能都在库`xscriptlib`中

> 你可以使用`import xscriptlib`来导入该库, 函数定义和用法都和python差不多

> 这门语言是设计为嵌入式的, 这样也可以保证安全以及运行时的效果

## 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`./xscript <file> [args...]`来运行.

当然, 你可以看看`xscript/examples`目录下的例子.

## 如何调试我的代码?
在`2020-5-10`次提交中更新了 debug 的用法.

现在允许你与 debug 交互.

请参阅[使用debug](learn/use-debug.md).

## 它有多快?
经过多次对比: python 比 xscript 快了一秒左右(`script/circle.xs`和基本上相同的python代码)

## 学习, 改进 xscript
xscript是一门开源编程语言, 它现在还处于开发阶段, 希望你能帮助改进xscript.

  - [报告一个BUG](bug.md)
  - [学习xscript](learn/index.md)
  - [xscript实现细节](xscript-in-detail/index.md)

!!! warning "特别注意"
	xscript 0.5 只是测试版本, 有很多问题没有上传到 issues, 请慎重使用 xscript.

- - -

非常抱歉, xscript 文档是简体中文版的, 请大家谅解. 你可以使用 Google Chrome 的翻译功能来阅读文档.

xscript 文档的多语种版本是有帮助的, 希望您能够将该文档翻译成相应的语言.
