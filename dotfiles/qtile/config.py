""" JMB config

author: Juan M. Barrios <juan.barrios@conabio.gob.mx>
"""

from typing import List  # noqa: F401
import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.log_utils import logger
# from libqtile.utils import guess_terminal

# Set variables
MOD = "mod4"
MYTERM = "kitty"
MYFONT = "JetBrains Mono"

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

# terminal = guess_terminal()

# Keymaps
keys = [
    # Monad tall keybindigs

    # Navigation
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows
    Key([MOD, "shift"], "h", lazy.layout.swap_left()),
    Key([MOD, "shift"], "l", lazy.layout.swap_right()),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),

    # Change windows sizes
    Key([MOD], "i", lazy.layout.grow()),
    Key([MOD], "d", lazy.layout.shrink()),
    Key([MOD], "n", lazy.layout.normalize()),
    Key([MOD], "o", lazy.layout.maximize()),
    Key([MOD, "shift"], "space", lazy.layout.flip()),

    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([MOD, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume 5")),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(),
    #     desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Keyboard layout
    Key([MOD, "shift"], "space", lazy.widget["keyboardlayout"].next_keyboard()),

    # Custom applications
    Key([MOD], "Return", lazy.spawn(MYTERM), desc="Launch terminal"),
    Key([MOD], 'r', lazy.spawn("rofi -show combi"), desc="Launch application launcher")
]

# Groups
activities = {
    "m": Group("main"),
    "w": Group("web"),
    "e": Group("editor"),
    "u": Group("music"),
    "s": Group("stream"),
    "c": Group("chat"),
}

groups = list(activities.values())

for k, g in activities.items():
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([MOD], k, lazy.group[g.name].toscreen(),
            desc=f"Switch to group {g.name}"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([MOD, "shift"], k, lazy.window.togroup(g.name, switch_group=True),
            desc=f"Switch to & move focused window to group {g.name}"),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

# Theme
layout_theme = dict(
    border_width=3,
    margin=7,
    border_focus=GREEN,
    border_normal=BLACK,
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
    layout.Floating(border_width=3, border_focus=GREEN, border_normal=BLACK)
]

widget_defaults = dict(
    font=MYFONT,
    fontsize=14,
    padding=5,
    background=BLACK,
    foreground=GRAY,
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
                    active=GRAY,
                    inactive=DGRAY,
                    block_highlight_text_color=BLACK,
                    highlight_method='block',
                    this_current_screen_border=GREEN,
                    this_screen_border=BLUE,
                ),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Net(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Battery(format=' {char} {percent:2.0%}'),
                widget.PulseVolume(),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "es"],
                    background=YELLOW,
                    foreground=BLACK,
                ),
                widget.QuickExit(
                    default_text="[ Bye ]",
                    background=ORANGE,
                    foreground=BLACK,
                ),
                widget.CurrentLayout(
                    background=RED,
                    foreground=BLACK
                ),
            ],
            24,
        ),
        wallpaper='~/Pictures/destiny-2-2019-game-wallpapers.jpg',
        wallpaper_mode='fill',
    ),
    Screen(
        top=bar.Gap(5),
        right=bar.Gap(5),
        left=bar.Gap(5),
        bottom=bar.Gap(5),
        wallpaper='~/Pictures/destiny-2-2019-game-wallpapers.jpg',
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
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

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
