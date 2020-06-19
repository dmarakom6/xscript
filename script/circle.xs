# xscript/script/circle.xs

call xscript.turtle.color red yellow
call xscript.turtle.begin_fill
call xscript.turtle.speed 15
for i 0 360
    call xscript.turtle.forward 1
    call xscript.turtle.left 1
end for
call xscript.turtle.end_fill
exit 0
