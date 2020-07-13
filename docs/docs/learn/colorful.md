# 更漂亮的界面
> 使用`color`命令(`commit:2020-06-17`)

## 准备
为了使用`color`命令, 应该先安装`colorama`模块, 已经在安装的时候安装好了, 不必重复安装.

## 语法
*color $action [$args...]*

所有的颜色和样式的控制都符合上述的语法:

  - `action` - 子命令
  - `args` - 传递给子命令的参数(可选)

## 使用
初始化: *color init $args...*

  - `args` - `colorama.init`接收的参数, 会将`args`中提供的参数都设置为`&true`

改变前景颜色: *color setfore $color*

  - `color` - 是一个颜色字符串, 对应`colorama.Fore`中的颜色(一定要全部大写)

其他子命令:

  - *color setback $color* - 设置背景色
  - *color setstyle* - 设置样式
  - *color reset* - 将颜色和样式恢复正常(相当于`color setstyle RESET_ALL`)
