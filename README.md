> 这里是 xscript0.5, xIDE0.0 的 Github 仓库
# xscript 0.5
xscript 是用 python 编写的一个非常小巧的编程语言, 它的核心(`xscriptcore.py`)会很小.

没有函数, 没有判断结构. 它只有最基本的变量管理, 所有类型的循环结构, 可调用的外部函数(python 实现), 没了!

`xIDE`是xscript配套的IDE

> `xIDE`正在编写中, 请不要使用`xIDE`以及`xIDElib/`中的任何源代码.

xscript 的 python代码从来没有遵守 python 代码规范, xscript 的 xscript 代码不需要代码规范.

访问[xscript主页](https://jason-bowen-zheng.github.io/xscript)获取更多信息。

# 安装
先将该git库拷贝到线下:
```shell
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript/
```

然后请先安装xscript和它的依赖项:
```shell
# 需要使用root权限
pip install -U colorama mkdocs prettytable
sudo make install
```

最后你可以测试一下 xscript:
```shell
make demo
```

如果想要更新 xscript, 请输入:
```shell
sudo make upgrade
```

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`./xscript <file> [args...]`来运行.

当然, 你可以看看`xscript/examples`目录下的 xscript 脚本的例子.
