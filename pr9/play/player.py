import pygame
import os
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

font = pygame.font.SysFont("Arial", 24)

MUSIC_PATH = r"C:\Users\Termonigr228siko\Desktop\phy3\pr9\play"
playlist = [
    os.path.join(MUSIC_PATH, "Malenky.mp3"),
    os.path.join(MUSIC_PATH, "Dvory.mp3"),
    os.path.join(MUSIC_PATH, "Chip_dramy.mp3")
]

current = 0

playing = False
start_time = 0
paused_time = 0

def play_music():
    global playing, start_time
    file_path = playlist[current]
    if os.path.exists(file_path): 
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        playing = True
        start_time = time.time()
    else:
        print(f"Ошибка: Файл {file_path} не найден в {os.getcwd()}")


def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_track():
    global current
    current = (current + 1) % len(playlist)
    play_music()

def prev_track():
    global current
    current = (current - 1) % len(playlist)
    play_music()

running = True
while running:
    screen.fill((30, 30, 30))
    display_name = os.path.basename(playlist[current]) 
    track_text = font.render(f"Track: {display_name}", True, (255, 255, 255))
    screen.blit(track_text, (20, 50))

    status = "Playing" if playing else "Stopped"
    status_text = font.render(f"Status: {status}", True, (255, 255, 255))
    screen.blit(status_text, (20, 100))

    if playing:
        elapsed = int(time.time() - start_time)
        time_text = font.render(f"Time: {elapsed}s", True, (255, 255, 255))
        screen.blit(time_text, (20, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()

            if event.key == pygame.K_s:
                stop_music()

            if event.key == pygame.K_n:
                next_track()

            if event.key == pygame.K_b:
                prev_track()

            if event.key == pygame.K_q:
                running = False

    pygame.display.update()

pygame.quit()