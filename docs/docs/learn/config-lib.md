#自定义标准库
> 添加标准库源文件

## 编写文件
xscript可以但是不能完全使用python的源文件, 要适当重写.

如何重写:

  - 重写函数调用
  - xscript不能创建和调用python对象及其方法和变量, 请将创建对象的代码转换为一个返回该对象的函数, 添加函数以便使用对象的方法
  - 注意对传入参数的转换

!!! tips "贴示"
	在使用python库的时候应该对使用的库名进行更改:
	比如`os`换成`_os`

## 使用
请在`xscriptlib/__init__.py`中添加一行来import刚刚编写的库.

以一个`foo`为例子:

  1. 编辑`xscriptlib/__init__.py`
  2. 输入`import xscriptlib.foo as foo`
  3. 重启解释器
  4. 编写程序测试一下
  5. 完成
