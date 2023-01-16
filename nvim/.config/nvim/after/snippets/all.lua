local ls = require("luasnip")

return {
  ls.snippet(
    { trig = "jmb" },
    { ls.text_node("Juan M Barrios <juan.barrios@conabio.gob.mx>") }
  ),
}

