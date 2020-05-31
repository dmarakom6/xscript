# xscript/script/circle.xs

let speed #= 15
let radius #= 1
xscript.turtle.color red yellow
xscript.turtle.begin_fill
xscript.turtle.speed &speed
for i 0 360
    xscript.turtle.forward &radius
    xscript.turtle.left &radius
end for
xscript.turtle.end_fill
