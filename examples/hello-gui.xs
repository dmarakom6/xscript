# xscript/examples/hello-gui.xs

import x.ui

let win = '[call ui.Window]'
let l = '[call ui.Label &win]'
call l.configure text Hello
call l.pack
call win.mainloop
exit 0
