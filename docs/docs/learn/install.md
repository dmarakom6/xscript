# 安装 xscript
xscript 不需要安装, 但 xscript是 使用 python 编写的, 需要安装 python.

xscript 在 python3.8 中可以很好的运行, 所以请安装 python 的最新版本.

- - -

xscript 的最新版本托管在 Github 上, 请先 clone 该 git 库.

```
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript
```

或下载[zip文件](https://github.com/jason-bowen-zheng/xscript/archive/master.zip).

## Linux下安装
运行:
```shell
pip install -U colorama mkdocs prettytable
make install
```

## Windows 下安装
这个`Makefile`是为 Linux 写的, Windows 用户请输入如下命令:
```shell
# 如果 Windows 上有 make 命令可直接输入 make install
pip install -U colorama mkdocs prettytable
python setup.py install
```

## 更新
运行:
```shell
make up
```
