require('jmbarrios.plugins')
require('jmbarrios.lsp')
require('jmbarrios.snip')

vim.cmd[[
  augroup Packer
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerCompile
  augroup end
]]

require('lualine').setup{
  options = {
    theme = 'sonokai',
  },
}

require('telescope').setup{
  defaults = {
    prompt_prefix = '$ ',
    file_ignore_patterns = {
      'node_modules'
    },
  }
}

require('telescope').load_extension('fzf')

-- Telescope mapping
vim.api.nvim_set_keymap('n', ' ff', '<cmd>Telescope find_files<cr>', {noremap=true})
vim.api.nvim_set_keymap('n', ' fg', '<cmd>Telescope live_grep<cr>', {noremap=true})
vim.api.nvim_set_keymap('n', ' fb', '<cmd>Telescope buffers<cr>', {noremap=true})
vim.api.nvim_set_keymap('n', ' fh', '<cmd>Telescope help_tags<cr>', {noremap=true})
