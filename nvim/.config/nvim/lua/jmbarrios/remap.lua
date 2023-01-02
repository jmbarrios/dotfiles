vim.keymap.set('n', '<leader>pv', vim.cmd.Ex);

vim.keymap.set('n', '<up>', '<nop>', {noremap = true});
vim.keymap.set('n', '<down>', '<nop>', {noremap = true});
vim.keymap.set('n', '<left>', '<nop>', {noremap = true});
vim.keymap.set('n', '<right>', '<nop>', {noremap = true});
vim.keymap.set('v', '<up>', '<nop>', {noremap = true});
vim.keymap.set('v', '<down>', '<nop>', {noremap = true});
vim.keymap.set('v', '<left>', '<nop>', {noremap = true});
vim.keymap.set('v', '<right>', '<nop>', {noremap = true});

vim.keymap.set('i', 'jk', '<esc>', {noremap = true});

vim.keymap.set('n', '<c-h>', '<c-w>h',
                        {noremap = true, silent = true});
vim.keymap.set('n', '<c-j>', '<c-w>j',
                        {noremap = true, silent = true});
vim.keymap.set('n', '<c-k>', '<c-w>k',
                        {noremap = true, silent = true});
vim.keymap.set('n', '<c-l>', '<c-w>l',
                        {noremap = true, silent = true});

-- Edit init.lua
vim.keymap.set('n', '<leader>ev', ':e $MYVIMRC<cr>',
                        {noremap = true, silent = true});
vim.keymap.set('n', '<leader>sv', ':source $MYVIMRC<cr>',
                        {noremap = true, silent = true});

