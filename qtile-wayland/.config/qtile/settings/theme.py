# Theme loader inspired on Antonio Sarosi theme loader

# Theming for Qtile

import json

from .paths import qtile_path


def load_theme():
    theme = "tokyo_night"

    theme_path = qtile_path / "themes"

    theme_file = theme_path / f'{theme}.json'
    if not theme_file.is_file():
        raise Exception(f'"{theme_file}" does not exist')

    with open(theme_file) as f:
        return json.load(f)


if __name__ == "settings.theme":
    colors = load_theme()
