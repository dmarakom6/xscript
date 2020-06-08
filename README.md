# 什么是xscript?
xscript是用python编写的一个非常小巧的编程语言, 它的核心(`core.py`)会很小.

没有函数, 没有判断结构. 它只有最基本的变量管理, 所有类型的循环结构, 可调用的外部函数(python实现), 没了!

# 安装
先将该git库拷贝到线下:
```shell
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript/
```

然后请先安装`prettytable`的python模块:
```shell
pip install -U prettytable
```

最后你可以测试一下xscript:
```shell
xscript script/hello.xs
```

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`xscript <file> [args...]`来运行.

当然, 你可以看看`xscript/script`目录下的例子.

## 如何调试我的代码?
在`2020-5-10`次提交中更新了debug的用法.

现在允许你与debug进行简单但有用的交互.

# 它有多快?
求xscript运行时有多快是一件麻烦的事情, 我们不高兴做这些没有意义的事情.
