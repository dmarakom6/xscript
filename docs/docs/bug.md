# 报告BUG
你可以点击`Issues`选项卡, 输入问题后提交就可以了.
> 真的非常感谢!!

#已知的BUG
- 文件`xscript/xscript/ui.py`, 所有小部件(`Label`, `Button`等).
  
  在如下代码中:

  ```
  let win := [xscript.ui.Window]
  let label := ['xscript.ui.Label $win']
  xscript.ui.pack $label
  ```

  会引发如下错误(在GUI环境下):

  ```
  Traceback:
  line 2
  ->  let l := ['xscript.ui.Label $win']
  Error: can only concatenate str (not "int") to str
  ```
  
  - - -
