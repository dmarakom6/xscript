" Vim syntax file
" Language:	xscript
" Maintainer:	jason-bowen-zheng
" Last Change:	2020 Jul 11

if exists("b:current_syntax")
	finish
endif

" key word
syntax keyword	xscriptInclude	import
syntax keyword	xscriptKeyWord	assert end delete let
syntax keyword	xscriptKeyWord	true false null argv interpreter
syntax keyword	xscriptOperator	is in !is !in
syntax keyword	xscriptRepeat	for foreach
syntax keyword	xscriptCmd	call color debug exit gets puts

" string
syntax region	xscriptString	start='"' end='"' fold
syntax region	xscriptString	start="'" end="'" fold
syntax keyword	xscriptTodo	FIXME NOTE NOTES TODO XXX contained
syntax match	xscriptComment	"^#.*$" contains=xscriptTodo

" number
syntax match	xscriptNumber	"^(\+|-)?[0-9]*$" display contained
syntax match	xscriptNumber	"^(\+|-)?[0-9]*\.[0-9]*" display contained

" highlight links
highlight def link xscriptInclude	Include
highlight def link xscriptKeyWord	Statement
highlight def link xscriptOperator	Operator
highlight def link xscriptRepeat	Repeat
highlight def link xscriptCmd		Function
highlight def link xscriptString	String
highlight def link xscriptTodo		Todo
highlight def link xscriptComment	Comment
highlight def link xscriptNumber	Number

let b:current_syntax = "xscript"
