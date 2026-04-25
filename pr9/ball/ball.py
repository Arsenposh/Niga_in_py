import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving ball")
clock = pygame.time.Clock()

x, y = 800 // 2, 600 // 2
radius = 25
step = 20 
color = (255, 155, 0)

running = True
while running:
    screen.fill((255, 255, 255)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x-step >= radius:
                    x-=step
            if event.key == pygame.K_RIGHT:
                if x +step <= 800 - radius:
                    x+= step

            if event.key == pygame.K_UP:
                if y - step >= radius:
                    y -= step
            
            if event.key == pygame.K_DOWN:
                if y + step <= 600 - radius:
                    y += step

    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)