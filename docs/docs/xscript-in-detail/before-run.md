# 运行前
> xscript 运行前准备

## xscript.main()
`main`函数是 xscript 的主函数, 它负责解析命令行和启动解释器.
> `xscript`命令仅仅需提供最简单的运行脚本的 xscript 脚本路径及其参数, 不提供返回 xscript 版本号的参数, 请自行查看 `xscriptcore.py`, 或运行: `xscript examples/getver.xs`查询.

## xscrptcore.\_\_init\_\_(), xscriptcore.restart()
这两个函数是一样的, `xscriptcore.__init__`会调用`xscriptcore.restart`函数, 它主要设置一些解释器运行时变量, 但是不启动解释器.
