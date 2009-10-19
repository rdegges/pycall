" .vimrc
"
" @author:	Randall Degges
" @email:	rdegges@gmail.com
" @date:	7-22-09
"
" This vim configuration file contains my vim configs which are used in all of
" my projects. These are sane, programmer settings which help view and modify
" code quickly and easily. To view the code in this project best, use these
" configs.

" search options
set is		" set incremental search
set ic		" set ignore case when searching
set scs		" set smartcase (if the search string has uppercase letters, assume
			" it IS case sensitive)
" text display
set wrap	" turn long line wrapping on
set ts=4	" display tabs with a width of 4

" color display
set bg=dark	" dark or light-- use dark background and light text
syntax on	" turn on syntax highlighting

" indentation
set ai		" turn automatic indenting on
set si		" turn smart indenting on
