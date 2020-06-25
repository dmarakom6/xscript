# 更多功能
> 导入外部函数库

## 为什么?
导入一个包能方便编写程序, 你肯定不希望写`call x.turtle.forward 100`, 而是喜欢`call turtle.forward 100`

庆幸的是, xscript拥有这种功能

## 我该怎么做?
很简单, xscript提供一`import`命令来导入包, 有两种选择:
> 以一个`foo`包为例

### 导入一个单一的包
`import foo`

如果`foo`是符合xscript命名规则的字符串, 那么xscript会直接导入`foo`

### 导入包中的包
`import foo.bar`

这里包及其附属的包必须使用`.`来分割, 不支持`*`, 以最终包的名字为变量(这里是`bar`)

!!! tips "注意"
	像`import 图像.Image`这样的包是允许导入的, xscript只检查最后一个名字(这里是`Image`)是否符合命名规则

## 特别注意!
`import`会在创建变量之前检查改要导入之物是否为一个包, 而不是函数, 类.
