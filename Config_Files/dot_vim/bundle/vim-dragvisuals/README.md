# DragVisuals

Vim global plugin for dragging virtual blocks

## Installation

Use [pathogen][3] or [vundle][4] to install vim-dragvisuals.vim.

  [3]: https://github.com/tpope/vim-pathogen
  [4]: https://github.com/gmarik/vundle

## Configuration

Add the following to your .vimrc:
```vim
Bundle 'pablobfonseca/vim-dragvisuals'

vmap  <expr>  <LEFT>   DVB_Drag('left')
vmap  <expr>  <RIGHT>  DVB_Drag('right')
vmap  <expr>  <DOWN>   DVB_Drag('down')
vmap  <expr>  <UP>     DVB_Drag('up')
vmap  <expr>  D        DVB_Duplicate()


" Remove any introduced trailing whitespace after moving
let g:DVB_TrimWS = 1

" Or, if you use the arrow keys for normal motions, choose
" four other keys for block dragging. For example:

vmap  <expr>  h        DVB_Drag('left')
vmap  <expr>  l        DVB_Drag('right')
vmap  <expr>  j        DVB_Drag('down')
vmap  <expr>  k        DVB_Drag('up')

" Or:

vmap  <expr>  <S-LEFT>   DVB_Drag('left')
vmap  <expr>  <S-RIGHT>  DVB_Drag('right')
vmap  <expr>  <S-DOWN>   DVB_Drag('down')
vmap  <expr>  <S-UP>     DVB_Drag('up')

" Or even:

vmap  <expr>   <LEFT><LEFT>   DVB_Drag('left')
vmap  <expr>  <RIGHT><RIGHT>  DVB_Drag('right')
vmap  <expr>   <DOWN><DOWN>   DVB_Drag('down')
vmap  <expr>     <UP><UP>     DVB_Drag('up')
```

## Credits
This plugin's owner is [Damian Conway ](http://damian.conway.org/), I just put
it on github.
