from typing import List, Optional
from libqtile.config import EzKey as Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


# Keymaps
KEYMAP = [
    # Navigation
    Key("M-h", lazy.layout.left(), desc="Move focus to left"),
    Key("M-l", lazy.layout.right(), desc="Move focus to right"),
    Key("M-j", lazy.layout.down(), desc="Move focus down"),
    Key("M-k", lazy.layout.up(), desc="Move focus up"),
    Key("M-<Space>", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows
    Key("M-S-h", lazy.layout.swap_left()),
    Key("M-S-r", lazy.layout.swap_right()),
    Key("M-S-j", lazy.layout.shuffle_down()),
    Key("M-S-k", lazy.layout.shuffle_up()),

    # Change windows sizes
    Key("M-i", lazy.layout.grow(), desc="Grow window size"),
    Key("M-d", lazy.layout.shrink(), desc="Shrink window size"),
    Key("M-n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key("M-o", lazy.layout.maximize(), desc="Maxime focused window"),
    Key("M-S-<Space>", lazy.layout.flip()),

    # Toggle between different layouts as defined below
    Key("M-<Tab>", lazy.next_layout(), desc="Toggle between layouts"),
    Key("M-x", lazy.window.kill(), desc="Kill focused window"),

    # Qtile tasks
    Key("M-C-r", lazy.restart(), desc="Restart Qtile"),
    Key("M-C-q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Sound
    Key("<XF86AudioMute>", lazy.spawn("pulsemixer --toggle-mute")),
    Key("<XF86AudioLowerVolume>", lazy.spawn("pulsemixer --change-volume -5")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("pulsemixer --change-volume 5")),

    # Keyboard layout
    Key("M-S-<Space>", lazy.widget["keyboardlayout"].next_keyboard()),

    # Custom applications
    Key('M-r', lazy.spawn("rofi -show combi"), desc="Launch application launcher"),

    # Screenlock
    Key('M-S-l', lazy.spawn("betterlockscreen -l blur"))
]
    

def get_keymap(mod_key: str="mod4", term: Optional[str]=None) -> List[Key]:
    """ Return keymap 

    Parameters
    ==========
    mod_key:
        mode key to set 
    term:
        terminal name

    Returns
    =======
    A list with a keymap
    """
    Key.modifier_keys.update({"M": mod_key})
    
    if not term:
        term = guess_terminal()
    
    KEYMAP.append(
        Key("M-<Return>", lazy.spawn(term), desc="Launch terminal")
    )

    return KEYMAP

