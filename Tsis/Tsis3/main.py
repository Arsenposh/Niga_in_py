import pygame
import sys
from pygame.locals import *

import ui
from ui import Button
from persistence import load_settings, save_settings, load_leaderboard, save_score
from kchau import run_game

SCREEN_W = 400
SCREEN_H = 600

pygame.init()
surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Racer — TSIS3")
ui.init_fonts()

settings = load_settings()

# Музыка
if settings["sound"]:
    try:
        pygame.mixer.music.load("background.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except:
        pass

def screen_main_menu():
    cx = SCREEN_W // 2
    buttons = [
        Button(cx - 100, 200, 200, 50, "Play",        ui.GREEN),
        Button(cx - 100, 270, 200, 50, "Leaderboard", ui.GRAY),
        Button(cx - 100, 340, 200, 50, "Settings",    ui.GRAY),
        Button(cx - 100, 410, 200, 50, "Quit",        ui.RED),
    ]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = event.pos
                if buttons[0].is_clicked(pos): return "play"
                if buttons[1].is_clicked(pos): return "leaderboard"
                if buttons[2].is_clicked(pos): return "settings"
                if buttons[3].is_clicked(pos):
                    pygame.quit(); sys.exit()

        ui.draw_main_menu(surface, buttons)
        pygame.display.flip()

def screen_enter_name():
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN and name.strip():
                    return name.strip()
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 12:
                    name += event.unicode

        ui.draw_name_screen(surface, name)
        pygame.display.flip()

def screen_game_over(score, distance, coins):
    cx = SCREEN_W // 2
    buttons = [
        Button(cx - 100, 420, 200, 50, "Retry",     ui.GREEN),
        Button(cx - 100, 490, 200, 50, "Main Menu", ui.GRAY),
    ]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = event.pos
                if buttons[0].is_clicked(pos): return "retry"
                if buttons[1].is_clicked(pos): return "menu"

        ui.draw_game_over(surface, score, distance, coins, buttons)
        pygame.display.flip()

def screen_leaderboard():
    back_btn = Button(SCREEN_W // 2 - 80, 540, 160, 45, "Back", ui.GRAY)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if back_btn.is_clicked(event.pos):
                    return

        lb = load_leaderboard()
        ui.draw_leaderboard(surface, lb, back_btn)
        pygame.display.flip()

def screen_settings():
    cx = SCREEN_W // 2
    buttons = [
        Button(cx - 100, 230, 200, 45, "Toggle Sound",      ui.GRAY),
        Button(cx - 100, 290, 200, 45, "Difficulty",        ui.GRAY),
        Button(cx - 100, 350, 200, 45, "Car Color",         ui.GRAY),
        Button(cx - 100, 430, 200, 45, "Back",              ui.GREEN),
    ]
    difficulties = ["easy", "normal", "hard"]
    car_colors   = ["blue", "red", "green"]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = event.pos
                if buttons[0].is_clicked(pos):
                    settings["sound"] = not settings["sound"]
                    if settings["sound"]:
                        try:
                            pygame.mixer.music.play(-1)
                        except: pass
                    else:
                        pygame.mixer.music.stop()

                if buttons[1].is_clicked(pos):
                    idx = difficulties.index(settings["difficulty"])
                    settings["difficulty"] = difficulties[(idx + 1) % 3]

                if buttons[2].is_clicked(pos):
                    idx = car_colors.index(settings["car_color"])
                    settings["car_color"] = car_colors[(idx + 1) % 3]

                if buttons[3].is_clicked(pos):
                    save_settings(settings)
                    return

        ui.draw_settings(surface, settings, buttons)
        pygame.display.flip()

username = ""

while True:
    action = screen_main_menu()

    if action == "play":
        if not username:
            username = screen_enter_name()

        result = run_game(surface, settings, username)

        if result:
            save_score(username, result["score"], result["distance"])
            action = screen_game_over(result["score"], result["distance"], result["coins"])
            if action == "retry":
                result = run_game(surface, settings, username)
                if result:
                    save_score(username, result["score"], result["distance"])

    elif action == "leaderboard":
        screen_leaderboard()

    elif action == "settings":
        screen_settings()
