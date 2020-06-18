# 基本输入输出
基本输入输出是编程语言中最基本的东西, xscript包涵了内置的输入, 输出命令:

!!! warning "警告"
	xscript**很有可能**将这些东西从解释器核心中删除!

用户输入命令: *gets $prompt=?*

- *prompt* - 一个提示符

> 提示用户输入

gets命令的本质就是python的`input`函数, 所以应用起来很简单.

- - -

用户输出命令: *puts &args...*

- *args* - 一些参数

> 用户输出, 一般打印到控制台

puts命令的本质是python的`print`函数.

!!! tips "贴示"
	`puts`命令会在每个打印的参数后面追加空格, 打印完毕之后换行

- - -

!!! tips "另请参阅"
	[xscript.util](../lib/util.md)库中包涵了更方便的输入, 输出命令
