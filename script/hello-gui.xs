let win := [xscript.ui.Window]
let l := '[xscript.ui.Label $win]'
xscript.ui.configure $l text Hello
xscript.ui.pack $l
xscript.ui.mainloop $win
