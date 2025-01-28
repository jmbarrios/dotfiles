""" JMB config

author: Juan M. Barrios <juan.barrios@conabio.gob.mx>
"""

from typing import List  # noqa: F401
from pathlib import Path
import os
import subprocess

from libqtile import bar, widget, hook
from libqtile import layout
from libqtile.config import Click, Drag, Match, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from settings.keymap import get_keymap
from settings.groups import groups, groups_keymap
from settings.theme import colors 
# from libqtile.log_utils import logger

# Set variables
MOD = "mod4"
MYTERM = "kitty"
MYFONT = "JetBrainsMono Nerd Font"

# Define theme colors
MYCOLORS = [
    '#282828',
    '#cc241d',
    '#98971a',
    '#d79921',
    '#458588',
    '#b16286',
    '#689d6a',
    '#a89984',
    '#504945',
    '#d65d0e'
]

BLACK  = MYCOLORS[0]
RED    = MYCOLORS[1]
GREEN  = MYCOLORS[2]
YELLOW = MYCOLORS[3]
BLUE   = MYCOLORS[4]
PURPLE = MYCOLORS[5]
AQUA   = MYCOLORS[6]
GRAY   = MYCOLORS[7]
DGRAY  = MYCOLORS[8]
ORANGE = MYCOLORS[9]

keys = get_keymap(MOD, MYTERM)

# groups = groups
keys.extend(groups_keymap)

logger.warning(keys)
logger.warning(groups)


# Theme
layout_theme = dict(
    border_width=1,
    margin=4,
    border_focus=colors["focus"],
)

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(name='monad', **layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(border_width=1, border_focus=colors["focus"])
]

widget_defaults = dict(
    font=MYFONT,
    fontsize=14,
    padding=5,
    background=colors["dark"],
    foreground=colors["grey"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Gap(5),
        right=bar.Gap(5),
        left=bar.Gap(5),
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active=colors["active"],
                    inactive=colors["inactive"],
                    block_highlight_text_color=colors["text"],
                    highlight_method='block',
                    this_current_screen_border=colors["focus"],
                    this_screen_border=colors["grey"],
                ),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.Systray(),
                widget.Net(),
                widget.PulseVolume(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Battery(format=' {char} {percent:2.0%}'),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "es"],
                    background=colors["color2"],
                    foreground=colors["text"],
                ),
                widget.QuickExit(
                    default_text="[ Bye ]",
                    background=colors["color3"],
                    foreground=colors["text"],
                ),
                widget.CurrentLayout(
                    background=colors["color4"],
                    foreground=colors["text"]
                ),
            ],
            24,
        ),
        wallpaper='~/Pictures/Neomuna_Nights.jpg',
        wallpaper_mode='fill',
    ),
    Screen(
        top=bar.Gap(5),
        right=bar.Gap(5),
        left=bar.Gap(5),
        bottom=bar.Gap(5),
        wallpaper='~/Pictures/Neomuna_Nights.jpg',
        wallpaper_mode='fill',
    )
]

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]

# Autostart
@hook.subscribe.startup_once
def autostart():
    os.environ["XDG_CURRENT_DESKTOP"] = "QTILE"
    p = subprocess.Popen(
        [
            "systemctl",
            "--user",
            "import-environment",
            "WAYLAND_DISPLAY",
            "XDG_CURRENT_DESKTOP",
        ],
    ).wait()
    home = Path.home() / '.config' / 'qtile' / 'autostart.sh'
    subprocess.run([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
