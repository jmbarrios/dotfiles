local ls = require("luasnip")
-- local types = require("luasnip.util.types")
local s = ls.snippet
-- local sn = ls.snippet_node
local t = ls.text_node
-- local i = ls.insert_node
-- local f = ls.function_node
-- local c = ls.choice_node
-- local d = ls.dynamic_node
-- local r = ls.restore_node
-- local l = require("luasnip.extras").lambda
-- local rep = require("luasnip.extras").rep
-- local p = require("luasnip.extras").partial
-- local m = require("luasnip.extras").match
-- local n = require("luasnip.extras").nonempty
-- local dl = require("luasnip.extras").dynamic_lambda
-- local fmt = require("luasnip.extras.fmt").fmt

ls.config.set_config {
  history = true,
  updateevents = "TextChanged,TextChangedI",
}

vim.api.nvim_set_keymap('n', '<leader><leader>s', '<cmd>source ~/.config/nvim/lua/snip.lua<CR>', {})

-- local function copy(args)
--   return args[1]
--end

ls.snippets = {
  all = {
  },
  javascript = {
    s("imr", t("import React from 'react';")),
  },
}

require('luasnip.loaders.from_vscode').load()
require('luasnip.loaders.from_vscode').load({ paths = { './my-snippets' } })
