# 安装xscript
xscript不需要安装, 但xscript是使用python编写的, 需要安装python.

xscript在python3.8中可以很好的运行, 所以请安装python的最新版本.

- - -

xscript的最新版本托管在Github上, 请先clone该git库.

```
git clone https://github.com/jason-bowen-zheng/xscript
cd xscript
```

或下载[zip文件](https://github.com/jason-bowen-zheng/xscript/archive/master.zip).

## Linux下安装
运行:
```shell
make install
```

## Windows下安装
这个`Makefile`是为Linux写的, Windows用户请输入如下命令:
```shell
pip install -U prettytable mkdocs
python setup.py install
```

## 更新
运行:
```shell
make up
```
