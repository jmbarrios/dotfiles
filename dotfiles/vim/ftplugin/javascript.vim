" Indentation
setlocal shiftwidth=2
setlocal tabstop=2
setlocal softtabstop=2

" Code folding
syntax region foldBraces   start=+{+  end=+}+  fold transparent keepend extend
setlocal foldmethod=syntax
setlocal foldlevel=99
