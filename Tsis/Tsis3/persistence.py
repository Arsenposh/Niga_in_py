import json
import os

LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS = {
    "sound": True,
    "difficulty": "normal",  # easy / normal / hard
    "car_color": "blue"       # blue / red / green
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(name, score, distance):
    lb = load_leaderboard()
    lb.append({"name": name, "score": score, "distance": distance})
    # Сортируем по score, оставляем топ 10
    lb = sorted(lb, key=lambda x: x["score"], reverse=True)[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(lb, f, indent=2)
