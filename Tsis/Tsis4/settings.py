import json
import os

SETTINGS_FILE = "settings.json"


DEFAULT_SETTINGS = {
    "snake_color": [0, 255, 0],   
    "grid_overlay": False,
    "sound": False
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)

        for key, value in DEFAULT_SETTINGS.items():
            if key not in settings:
                settings[key] = value
        return settings

    return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)