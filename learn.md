# xscript
xscript是一个和tcl类似的命令语言, 使用python编写.

# xscript命令
xscript解释器执行命令之前需要做一些准备:

  0. 打开文件
  1. 将源文件中的诸如`\r\n`的换行符替换为`\n`
  2. 将#1的结果以`\n`为界, 分割成列表
  3. 将初始行号设置为0
  4. 运行!

## 如何写命令?
xscript的命令以空格分隔命令动词及其各个参数, 但会跳过第一个非空字符前的空字符(空格, TAB键).
如果参数中有空格, 请使用`'`或`"`将参数括住, 例:
```
puts "Hello, World!"
```
解释器会将它翻译成: `['puts', 'Hello, World!']`
其中, puts是命令动词, `Hello, World!`是其参数.

xscript支持的命令动词有:

|      |         |      |         |
| ---- | ------- | ---- | ------- |
| \#   | delete  | elif | else    |
| end  | exit    | for  | foreach |
| gets | if      | lets | puts    |
|while | xscript.|      |         |

> 注意, `xscript.`是一个单独的命令动词, 点后不允许有空格, 如`xscript.ui.Window`是正确的, `xscript. ui.Window`是错误的.

接下来, 我们将要一个一个解释着张表格中的命令动词.

## 注释
xscript的注释单独成行, 以`#`开头, 有如下要求:
  - \#号必须是第一个非空字符
  - 该行后即使有命令也不会被解释
