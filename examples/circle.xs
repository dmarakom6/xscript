# xscript/examples/circle.xs

import x.turtle

call turtle.color red yellow
call turtle.begin_fill
call turtle.speed 15
for i 0 360
    call turtle.forward 1
    call turtle.left 1
end for
call turtle.end_fill
gets :
exit 0
