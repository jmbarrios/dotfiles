from libqtile.config import Group, EzKey as Key
from libqtile.lazy import lazy


activities = {
    "m": Group("main"),
    "w": Group("web"),
    "e": Group("editor"),
    "u": Group("music"),
    # "s": Group("stream"),
    "c": Group("chat"),
}

groups = list(activities.values())

groups_keymap = [
    Key(f"M-{k}", lazy.group[g.name].toscreen(),
        desc=f"Switch to group {g.name}")
    for k, g in activities.items()
]
groups_keymap.extend([
    Key(f"M-S-{k}", lazy.window.togroup(g.name, switch_group=True),
        desc=f"Switch to & move focused window to group {g.name}")
    for k, g in activities.items()
])
