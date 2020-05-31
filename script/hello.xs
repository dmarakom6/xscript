# xscript/script/hello.xs

let ans = &null
while $ans != bye
    let ans = ['gets ?']
    puts input: &ans
end while
puts bye
