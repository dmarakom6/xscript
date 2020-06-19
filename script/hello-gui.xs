# xscript/script/hello-gui.xs

let win = '[call xscript.ui.Window]'
let l = '[call xscript.ui.Label &win]'
call xscript.ui.configure &l text Hello
call xscript.ui.pack &l
call xscript.ui.mainloop &win
exit 0
