import pygame
import datetime
import os
folder = os.path.dirname(__file__)
os.chdir(folder)

pygame.init()
WIDTH, HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
clock_img = pygame.image.load("clock.png").convert_alpha()
right_hand = pygame.image.load("rightarm.png").convert_alpha()
left_hand = pygame.image.load("leftarm.png").convert_alpha()
center = (WIDTH // 2, HEIGHT // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = - (minutes * 6) 
    second_angle = - (seconds * 6)

    rotated_min = pygame.transform.rotate(right_hand, minute_angle)
    rotated_sec = pygame.transform.rotate(left_hand, second_angle)

    offset_y = -100 

    min_rect = rotated_min.get_rect(center=(center[0], center[1] + offset_y))
    sec_rect = rotated_sec.get_rect(center=(center[0], center[1] + offset_y))

    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    screen.blit(rotated_min, min_rect)
    screen.blit(rotated_sec, sec_rect)

    pygame.display.update()
    clock.tick(60)