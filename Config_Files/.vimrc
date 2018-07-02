"cp .vimrc ~/.vimrc Copies vimrc to home dir
"
"https://dougblack.io/words/a-good-vimrc.html
"Link to a for helpful vim stuff

set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)
Plugin 'scrooloose/nerdtree'
Plugin 'jacoborus/tender.vim' "Color scheme
Plugin 'vim-airline/vim-airline'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'vim-dragvisuals.vim'


" ...
" All of your Plugins must be added before the following line

call vundle#end()            " required
filetype plugin indent on    " required

" autocmd vimenter * NERDTree " Opens NERDTree when vim starts
map <C-m> :NERDTreeToggle<CR>


set number " Turn's on number
"set relativenumber
set numberwidth=1 " Set number gutter width
set expandtab " Use spaces instead of tabs. Tab is just 4 spaces now
set tabstop=4
set shiftwidth=4 
set listchars=eol:¬,tab:>·,trail:~,extends:>,precedes:<,space:␣
set list

" Extra
syntax on " Eables syntax highlighting
" colorscheme afterglow
if (has("termguicolors"))
 set termguicolors
endif
colorscheme tender
set nowrapscan " This is so searching doesn't wrap around and continue. When reach EOF it'll stop
set cursorline " Shows a line under current line
set wildmenu " Helpful autocomplete menu
set lazyredraw " Faster macros
set showmatch " Show matching () [] {}
set hlsearch " Highlights search
set incsearch " Search while typing
" Stops search highlihting with shorcut , Space
nnoremap <leader><space> :nohlsearch<CR>

" Split 
set splitbelow
set splitright

" ===== Editing
set foldenable " Allows folding
set foldlevelstart=10
set foldnestmax=10 " Max folding nest level
set foldmethod=indent " Fold according to indentation
nnoremap <space> za
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview

" ===== Key Mapping
nnoremap j gj
nnoremap k gk
" g V visually shows block of text last added in INSERT
nnoremap gV `[v`]
inoremap jj <Esc>
nnoremap ; :

set spelllang=en_us         " spell checking
set encoding=utf-8 nobomb   " BOM often causes trouble, UTF-8 is awsum.

set autoread " reload file if changed exterally
set laststatus=2
set report=0
set showmode " Shows current mode
set title " Show file name
set modeline " Disabled mode line, for security reasons mostly
" Use ; for commands instead of ;. ex. ;wq not :wq no need for shift :)
set pastetoggle=<F2>
set showcmd " Shows last used command
set encoding=utf-8

highlight ColorColumn ctermbg=grey
call matchadd('ColorColumn', '\%81v', 100) " Only shows grey column bar if line text is breaking 80 char. for ex here :)
"
" Flashes next search in red
function! HLNext (blinktime)
    let [bufnum, lnum, col, off] = getpos('.')
    let matchlen = strlen(matchstr(strpart(getline('.'),col-1),@/))
    let target_pat = '\c\%#\%('.@/.'\)'
    let ring = matchadd('WhiteOnRed', target_pat, 101)
    redraw
    exec 'sleep ' . float2nr(a:blinktime * 1000) . 'm'
    call matchdelete(ring)
    redraw
endfunction

Bundle 'pablobfonseca/vim-dragvisuals'

vmap  <expr>  <LEFT>   DVB_Drag('left')
vmap  <expr>  <RIGHT>  DVB_Drag('right')
vmap  <expr>  <DOWN>   DVB_Drag('down')
vmap  <expr>  <UP>     DVB_Drag('up')
vmap  <expr>  D        DVB_Duplicate()


" Remove any introduced trailing whitespace after moving
let g:DVB_TrimWS = 1
