# end
`end` is a block end flag. `if`, `for` and `while` flag use `end` flag.

# for
`for` is a loop flag, it takes 3 or 4 arguments:

`for <variable> <from> <to> [<step>]`

`variable` will store in `self.itervar`, not `self.var`. So dont use `let` to change it, **Nothing meaningful!**
It's a range_iterator object. `for_flag` will manage it.

## Next is important, take careful!

`for_flag` is a very long function, the important thing is:

```python
nextvar = next(self.itervar[name], None)
self.var[name] = nextvar
```

# xscript
