# file - 文件相关操作

*fileClose &fileobj*

  - *fileobj* - 一个文件对象

> 关闭一个文件

- - -

*fileFlush &fileobj*

  - *fileobj* - 一个文件对象

> 刷新一个文件

- - -

*fileOpen &name $mode=r*

  - *name* - 一个文件名
  - *mode* - 文件的打开模式

> 打开一个文件, 返回打开的文件对象.

> 如果文件不存在, 返回-1.

- - -

*fileRead &fileobj \#size=-1*

  - *fileobj* - 一个文件对象
  - *size* - 要读取的数量[默认为全部(-1)]

> 读取文件内容.

- - -

*fileWrite &fileobj $s*

  - *fileobj* - 一个文件对象
  - *s* - 要写入的字符(串)

> 写入文件, 返回写入字符数
