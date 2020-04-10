> I'm so sorry about delete the English version README.

# 定义

## 块(block)
块是一组代码, 由块开始符(flag)开始, 如`if`, `for`, `foreach`, `while` 或 `function`.

结束符只有`end`, 如`end if`, `end function`等.

块是可以嵌套的, 但不允许跨块嵌套.

## 应该还有...

## 程序内变量的定义
> 下表所以的变量都在XScriptInterpreter中

| 变量    | 类型 | 定义                                     |
| ------- | ---- | ---------------------------------------- |
| now     | int  | 它记录了当前行号(从0开始)                |
| block   | list | 它记录了当前行所处的块                   |
| program | list | 它记录了整个程序                         |
| var     | dict | 它记录了程序中所用的变量 `{name: value}` |
| itervar | dict | 它记录了程序中所用的可迭代的变量         |
| debug   | bool | 它决定了程序是否开启调试                 |