# util - 让简单的编程变得更简单

*gets $prompt=?*

  - *prompt* - 提示符

> 请求输入一个字符串

- - -

*getsInt $prompt=int?*

*getFile $prompt=file? $mode=r*

*getFloat $prompt=float?*

  - *prompt* - 提示符
  - *mode* - 文件打开模式

> 分别将输入转换为int类型, float类型, 以及按照文件名打开一个文件

> 失败都会返回`&null`

- - -

!!! tips "注意"
	`xscript.util`标准库还添加了一些诸如`chr`, `hex`, `round`的python标准库中的`builtins`的函数(`commit:2020-6-14`)
