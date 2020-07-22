> 这里是 xscript0.5, xIDE0.0 的 Github 仓库

> [English](./README.md) | 简体中文
# xscript v0.5
xscript 是用 python3 编写的一个非常小巧的编程语言, 它的核心(`xscriptcore.py`)很小.

`xIDE`是 xscript 配套的 IDE

访问[xscript主页](https://jason-bowen-zheng.github.io/xscript)获取更多信息。

# 安装
1. 先将该 git 库拷贝到线下:
```shell
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript/
```

2. 然后请先安装xscript和它的依赖项:
```shell
# 或许需要使用root权限
pip install -U colorama mkdocs prettytable
sudo make install
```

3. 查看 xscript 的 demo:
```shell
make demo
```

4. 如果想要更新 xscript, 请输入:
```shell
sudo make upgrade
```

# 如何运行我的代码?
你可以在xscript目录下, 通过终端输入`./xscript <file> [args...]`来运行.

当然, 你可以看看`xscript/examples`目录下的 xscript 脚本的例子.
