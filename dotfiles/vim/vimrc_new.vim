" Juan M Barrios vimrc
" Date: July, 2020

" Plug settings and installed plugins --------------- {{{
" Plugins will be downloaded under the specified directory.
call plug#begin('~/.vim/plugged')

" Declare the list of plugins.
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'dense-analysis/ale'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'ycm-core/YouCompleteMe', { 'do': './install.py --clang-completer --ts-completer' }
Plug 'lejafar/vim-pipenv-ycm'
Plug 'lervag/vimtex'
Plug 'scrooloose/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'tpope/vim-fugitive'
Plug 'jidn/vim-dbml'
" Plug 'lvht/phpcd.vim', { 'for': 'php', 'do': 'composer install' }
" Plug 'vimwiki/vimwiki'
" Plug 'junegunn/goyo.vim'
" Plug 'lejafar/vim-pipenv-ycm'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()
" }}}

" General
" Set localleader
let mapleader = ','
let maplocalleader = '-'

" Fast editing myvimrc
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

" Vimscript file settings
augroup filetype_vim
  autocmd!
  autocmd FileType vim setlocal foldmethod=marker
augroup END

" Disable arrow keys >:)
nnoremap <up> <nop>
vnoremap <up> <nop>
nnoremap <down> <nop>
vnoremap <down> <nop>
nnoremap <left> <nop>
vnoremap <left> <nop>
nnoremap <right> <nop>
vnoremap <right> <nop>

" Fast exit insert mode
inoremap jk <esc>

" Show line numbers
set number
set relativenumber

" Use spaces instead of tabs
set expandtab

" Be smart when using tabs ;)
set smarttab

" 1 tab == 2 spaces
set shiftwidth=2
set tabstop=2

set ai "Auto indent
set si "Smart indent
syntax on

" Smart way to move between windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" Smart way to split windows
map <C-\%> :split<cr>
map <C-\|> :vsplit<cr>

" GruvBox theme
try
  set background=dark
  let g:gruvbox_contrast_dark='hard'
  colorscheme gruvbox

  " Set a 80 char ruler
  set colorcolumn=80
  
catch
endtry

" Delete trailing white space on save, useful for Python and CoffeeScript ;)
func! DeleteTrailingWS()
  exe "normal mz"
  %s/\s\+$//ge
  exe "normal `z"
endfunc

autocmd BufWritePre *.py,*.js :call DeleteTrailingWS()

" Custom abbrevations {{{
iabbrev jmbconabio Juan M. Barrios <juan.barrios@conabio.gob.mx>
iabbrev jmbau Juan M. Barrios <j.m.barrios@gmail.com>
iabbrev <expr> datetoday strftime("%Y-%m-%d")
" }}}

" Airline settings --------------- {{{
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail_improved'
let g:airline#extensions#ale#enabled = 1
let airline#extensions#ale#error_symbol = 'E:'
let airline#extensions#ale#warning_symbol = 'W:'
let airline#extensions#ale#show_line_numbers = 1
let airline#extensions#ale#open_lnum_symbol = '(L'
let airline#extensions#ale#close_lnum_symbol = ')'
" }}}

" ALEsettings --------------- {{{
let g:ale_python_auto_pipenv = 1
" }}}

" CtrlP setting --------------- {{{
let g:ctrlp_max_depth = 10
let g:ctrlp_open_new_file = 't'
" Fix up down navigation
let g:ctrlp_prompt_mappings = {
  \ 'PrtSelectMove("j")':   ['<down>'],
  \ 'PrtSelectMove("k")':   ['<up>'],
  \ 'PrtExit()':            ['<c-c>', '<c-g>'],
  \ }
let g:ctrlp_custom_ignore = {
  \ 'dir':    '\v[\/](node_modules)|(\.(git))$',
  \ 'file':   '\v\.(class|pyc)$'
  \ }
" }}}

" YCM settings --------------- {{{
let g:ycm_autoclose_preview_window_after_completion = 1
augroup ycm
  autocmd!
  autocmd FileType javascript,python nnoremap <buffer> <leader>gd :YcmCompleter GoTo<cr>
  autocmd FileType javascript,python nnoremap <buffer> <leader>?  :YcmCompleter GetDoc<cr>
augroup END
" }}}

" Vimtex settings ------------ {{{
let g:tex_flavor = 'latex'
if !exists('g:ycm:ycm_semantic_triggers')
  let g:ycm_semantic_triggers = {}
endif
autocmd VimEnter * let g:ycm_semantic_triggers.tex=g:vimtex#re#youcompleteme
" }}}

" NERDTree ----------- {{{
map <C-n> :NERDTreeToggle<CR>
let g:NERDTreeGitStatusUseNerdFonts = 1
" }}}

" Vimtex
" let g:vimtex_view_general_viewer = 'evince'
" if !exists('g:ycm_semantic_triggers')
"   let g:ycm_semantic_triggers = {}
" endif
" let g:ycm_semantic_triggers.tex = g:vimtex#re#youcompleteme
" let g:vimtex_compiler_latexmk = {
"       \ 'options' : [
"       \   '-xelatex'
"       \ ]
"       \}


" VimWiki
" let g:vimwiki_list = [{
"       \ 'path': '~/vimwiki/',
"       \ 'path_html': '~/wiki_html',
"       \ 'auto_toc': 1,
"       \ 'nested_syntaxes': {
"       \   'py': 'python',
"       \   'java': 'java',
"       \   'js': 'javascript'
"       \ }
"       \ }]
