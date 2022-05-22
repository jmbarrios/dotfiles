" -----------------------------------------------------------------------------
" init.lua
" -----------------------------------------------------------------------------

lua require('jmbarrios');

" -----------------------------------------------------------------------------
" General setting
" -----------------------------------------------------------------------------
set number
set relativenumber
set expandtab
set smarttab
set shiftwidth=2
set tabstop=2

set ai
set si
syntax on

try
  " let g:gruvbox_contrast_dark='hard'
  " colorscheme gruvbox
  colorscheme sonoakai
  let g.sonoakai_style = 'shusia'

  set colorcolumn=80
catch
endtry

func! DeleteTrailingWS()
  exe "normal mz"
  %s/\s\+$//ge
  exe "normal `z"
endfunc

autocmd BufWritePre *.py,*.js :call DeleteTrailingWS()

let mapleader = "\<space>"

nnoremap <leader>ve :edit ~/.config/nvim/init.vim<cr>
nnoremap <leader>vs :source ~/.config/nvim/init.vim<cr>

nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
vnoremap <up> <nop>
vnoremap <down> <nop>
vnoremap <left> <nop>
vnoremap <right> <nop>

inoremap jk <esc>

nmap <silent> <C-h> <C-w>h
nmap <silent> <C-j> <C-w>j
nmap <silent> <C-k> <C-w>k
nmap <silent> <C-l> <C-w>l

" -----------------------------------------------------------------------------
"  Telescope
" -----------------------------------------------------------------------------

" nnoremap <leader>ff <cmd>Telescope find_files<cr>
" nnoremap <leader>fg <cmd>Telescope live_grep<cr>
" nnoremap <leader>fb <cmd>Telescope buffers<cr>
" nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" -----------------------------------------------------------------------------
"  ALE
" -----------------------------------------------------------------------------

" let g:ale_completion_enabled = 1
" let g:ale_completion_max_suggestions=10
" let g:ale_detail_to_floating_preview = 1
" let g:ale_floating_window_border = ['│', '─', '╭', '╮', '╯', '╰']
" let g:ale_lsp_suggestions = 1
" let g:ale_fixers = {}
" let g:ale_fixers.python = ['black']
" let b:ale_linters = {}
" let b:ale_linters.javascript = ['quick-lint-js']
" let g:ale_python_black_auto_pipenv = 1
" let g:ale_python_black_auto_poetry = 1
" set omnifunc=ale#completion#OmniFunc
" inoremap <silent> <C-Space> <C-X><C-O>
