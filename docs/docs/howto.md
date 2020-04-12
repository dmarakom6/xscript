# xscript如何工作

# 定义
xscript是一门类似于tcl的命令语言

- - -

下面的一些词在xscript中有特定的意思.

> 以下所有的函数和变量都在`core.XScriptInterpreter`中`

## 块(block)

## 变量代换符($)
`$`号是命令替换符, 使用`replacevar`函数来替换在`var`中的变量.

## 命令替换符([...])
`[`和`]`是成对的命令替换符,使用`replacefunction`来替换.

命令替换符支持如下命令:

  - gets
  - xscript.
