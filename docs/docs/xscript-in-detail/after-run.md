# 运行完毕
> xscript 运行完毕后处理

## xscriptcore.XScriptInterpreter.exit
`exit`函数调用 python 的`sys.exit`函数. 所以, 运行完毕后全权由 python 负责.
> 需要传入一个整型字符串如`XScriptInterpreter.exit('1')`, 不然会打印另一个`1`并报错.
