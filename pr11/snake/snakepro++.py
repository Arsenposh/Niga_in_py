import pygame
import sys
import random
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("pr10/snake/music.mp3")
pygame.mixer.music.play(-1)
CELL =20
COLS = 30
ROWS = 30
WIN_W = COLS * CELL
WIN_H = ROWS * CELL + 40
screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial", 48)
BG = (0, 0, 0)
WALL = (100, 100, 100)
SNAKE_C = (0, 200, 0)
FOOD_C = (255, 0, 0)
WHITE = (255, 255, 255)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
score = 0
level = 1
speed = 200
game_over = False
walls = set()
for c in range(COLS):
    walls.add((c, 0))
    walls.add((c, ROWS - 1))
for r in range(ROWS):
    walls.add((0, r))
    walls.add((COLS - 1, r))
snake = [(15, 15), (14, 15), (13, 15)]
direction = RIGHT
next_dir = RIGHT
def new_food():
    while True:
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        if (x, y) not in walls and (x, y) not in snake:
            return (x, y)

food = new_food()
timer = 0
while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r and game_over:
                game_over = False
                score = 0
                level = 1
                speed = 200
                snake = [(15, 15), (14, 15), (13, 15)]
                direction = RIGHT
                next_dir = RIGHT
                food = new_food()
                timer = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if not game_over:
                if event.key == K_UP and direction != DOWN:
                    next_dir = UP
                if event.key == K_DOWN and direction != UP:
                    next_dir = DOWN
                if event.key == K_LEFT and direction != RIGHT:
                    next_dir = LEFT
                if event.key == K_RIGHT and direction != LEFT:
                    next_dir = RIGHT

    if not game_over:
        timer += dt
        if timer >= speed:
            timer = 0
            direction = next_dir
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            if new_head in walls:
                game_over = True
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = new_food()
                    if score == 3:
                        level = 2
                        speed = 160
                    if score == 7:
                        level = 3
                        speed = 120
                    if score == 12:
                        level = 4
                        speed = 90
                    if score == 18:
                        level = 5
                        speed = 65
                else:
                    snake.pop()

    screen.fill(BG)

    for (wc, wr) in walls:
        pygame.draw.rect(screen, WALL, (wc * CELL, 60 + wr * CELL, CELL, CELL))

    pygame.draw.rect(screen, FOOD_C, (food[0] * CELL, 60 + food[1] * CELL, CELL, CELL))

    for i, (sc, sr) in enumerate(snake):
        pygame.draw.rect(screen, SNAKE_C, (sc * CELL, 60 + sr * CELL, CELL, CELL))

    pygame.draw.rect(screen, (30, 30, 30), (0, 0, WIN_W, 60))
    score_text = font1.render("Score: " + str(score), True, WHITE)
    level_text = font1.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 18))
    screen.blit(level_text, (WIN_W - 120, 18))

    if game_over:
        text1 = font2.render("GAME OVER", True, (255, 0, 0))
        text2 = font1.render("press R to restart", True, WHITE)
        screen.blit(text1, (WIN_W // 2 - text1.get_width() // 2, WIN_H // 2 - 40))
        screen.blit(text2, (WIN_W // 2 - text2.get_width() // 2, WIN_H // 2 + 20))

    pygame.display.update()