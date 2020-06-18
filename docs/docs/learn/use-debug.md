# 使用debug
> debug命令是内嵌在解释器核心中的简单调试器

## 启动debug
xscript有一独立命令`debug`来启动debug. 会以横跨终端两段的`=`字符以及在`=`中居中的`start debug`和`end debug`来区分程序运行输出和debug输出.

!!! tips "贴示"
	在不支持`os.get_terminal_size`的平台上, 会以`xscript: start debug`和`xscript: end debug`来分隔

## debug命令

- *exit* - 退出debug
- *now* - 显示现在位于的块
> `now`会读取`core.XScriptInterpreter.block`中的数据, 以`.`分隔

- *ls* - 显示所有变量
- *show $name* - 只显示名字为`name`的变量
