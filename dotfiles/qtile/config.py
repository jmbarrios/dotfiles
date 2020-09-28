# JMB qtile conf file

import os
import subprocess
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

# Defining variables
MOD = "mod4"
MYTERM = 'alacritty'
MYAPPLAUNCHER = 'rofi'
MYFONT = 'Hack'
# terminal = guess_terminal()
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

# Keymaps
keys = [
    # Monad tall keybindings

    # Navigation
    Key([MOD], "h", lazy.layout.left()),
    Key([MOD], "l", lazy.layout.right()),
    Key([MOD], "j", lazy.layout.down()),
    Key([MOD], "k", lazy.layout.up()),

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

    Key([MOD, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    # Key([MOD], "r", lazy.spawncmd(),
    #     desc="Spawn a command using a prompt widget"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume 5")),

    # Keyboard layout
    Key([MOD, "shift"], "space", lazy.widget["keyboardlayout"].next_keyboard()),

    # Custom applications
    Key([MOD], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([MOD], "Return", lazy.spawn(MYTERM), desc="Launch terminal"),
    Key([MOD], "r", lazy.spawn("rofi -show combi"), desc="Launch rofi"),
]

# Keybiding for float
for key, x, y in [("Left", -10, 0),
                  ("Right", 10, 0),
                  ("Up", 0, -10),
                  ("Down", 0, 10)]:
    keys.append(Key([MOD, "control"], key, lazy.window.move_floating(x, y)))
    keys.append(Key([MOD, "shift"], key, lazy.window.resize_floating(x, y)))
    keys.append(Key([MOD, "mod1"], key, lazy.window.move_to_screen_edge(key)))

# Groups
activities = {
        'm': Group('main'),
        'w': Group('web', matches=[Match(wm_class=["firefox"])]),
        'e': Group('editor', matches=[Match(wm_class='Alacritty')]),
        'u': Group('music'),
        'c': Group('chat', matches=[Match(wm_class="teams")])
}

groups = [ g for g in activities.values() ]
for k, g in activities.items():
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([MOD], k, lazy.group[g.name].toscreen(),
            desc="Switch to group {}".format(g.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([MOD, "shift"], k, lazy.window.togroup(g.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(g.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

# Theme
layout_theme = {
    'border_width': 3,
    'margin': 7,
    'border_focus': GREEN,
    'border_normal': BLACK
}

layouts = [
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(name='monad', **layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(border_width=3, border_focus=GREEN, border_normal=BLACK),
]

widget_defaults = dict(
    font=MYFONT,
    fontsize=12,
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
                widget.Prompt(
                    background=BLUE,
                    foreground=BLACK,
                ),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Net(interface=["wlp2s0", "enp3s0"]),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Battery(format='Batt {char} {percent:2.0%}'),
                widget.PulseVolume(),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'es'],
                    background=YELLOW,
                    foreground=BLACK,
                ),
                widget.QuickExit(
                    default_text='[ Bye ]',
                    background=ORANGE,
                    foreground=BLACK,
                ),
                widget.CurrentLayout(
                    background=RED,
                    foreground=BLACK,
                ),
            ],
            24,
        ),
        wallpaper='~/Pictures/google-earth-view-2312.jpg',
        wallpaper_mode='fill',
    ),
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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
