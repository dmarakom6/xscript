# 基于tk的GUI库

该标准库使用python的tkinter库编写, 去除了一些复杂的选项.

*askyesno \#mesage\# \#title=xscript\#*
  
  - *message* - 要显示的信息
  - *title* - 消息框的标题

> 显示一个消息框

- - -

*Button \#master\#*
  
  - *master* - 小部件要显示的窗口

> 返回一个在master上的按钮

- - -

*configure \#widget\# \#item\# \#value\#*
  
  - *widget* - 要配置的小部件
  - *item* - 要配置的项目
  - *value* - item的值

> 设置widget, 相当于`widget[item] = value`

- - -

*destroy \#widget\#*
  
  - *widhet* - 一个小部件

> 从窗口删除一个小部件

- - -

*grid \#widget\# \#col\# \#row\#*
  
  - *widget* - 要显示的小部件
  - *col* - 要显示的列
  - *row* - 要显示的行

> 以网格形式来管理小部件
  
- - -

*Label \#master\#*

  - *master* - 小部件要显示的窗口

> 返回一个在master上的标签

- - -

*mainloop \#master\#*

  - *master* - 一个窗口对象

> 让master进入主循环

- - -

*showinfo \#message\# \#title=xscript\#*
  
  - *message* - 要显示的信息
  - *title* - 窗口的标题

> 显示一个消息框

- - -

*title \#widget\# \#title\#*
  
  - *widget* - 一个窗口对象
  - *title* - 窗口的标题

> 设置或返回widget的标题

- - -

*Window*
  
  - *没有参数*

> 创建并返回一个窗口对象用于后续操作
