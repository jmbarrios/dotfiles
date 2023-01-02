local telescope = require('telescope')

telescope.setup{
  defaults = {
    file_ignore_patterns = {
      'node_modules'
    }
  }
}

telescope.load_extension('fzf')

local builtin = require('telescope.builtin')

-- Telescope mappings
vim.keymap.set('n', '<leader>pf', builtin.find_files)
vim.keymap.set('n', '<leader>pb', builtin.buffers)
vim.keymap.set('n', '<leader>ps', function()
  builtin.grep_string({ search = vim.fn.input('Grep > ') });
end)
