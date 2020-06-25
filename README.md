> 这里是xscript0.5, xIDE0.0的Github仓库
# xscript 0.5
xscript是用python编写的一个非常小巧的编程语言, 它的核心(`xscriptcore.py`)会很小.

没有函数, 没有判断结构. 它只有最基本的变量管理, 所有类型的循环结构, 可调用的外部函数(python实现), 没了!

`xIDE`正在编写中, 估计在一个月里面完不成, 请不要使用`xIDE`以及`xIDElib/`中的任何源代码.

# 安装
先将该git库拷贝到线下:
```shell
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript/
```

然后请先安装xscript:
```shell
make install
```

最后你可以测试一下xscript:
```shell
make demo
```

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`./xscript <file> [args...]`来运行.

当然, 你可以看看`xscript/examples`目录下的例子.
