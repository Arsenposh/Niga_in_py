import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    help_font = pygame.font.SysFont("Arial", 16)
    
    radius = 15
    mode = 'blue'
    modi = 'circle' 
    points = []
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                
                elif event.key == pygame.K_1:
                    modi = 'square'
                elif event.key == pygame.K_2:
                    modi = 'triangle_right'
                elif event.key == pygame.K_3:
                    modi = 'triangle_eq'
                elif event.key == pygame.K_4:
                    modi = 'rhombus'
                elif event.key == pygame.K_5:
                    modi = 'circle'
            
            # изменение размера кисти
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            # движение мыши
            if event.type == pygame.MOUSEMOTION:
                # смещаем вниз, чтобы не рисовать на панели
                position = (event.pos[0], event.pos[1] + 60)
                points.append((position, mode, modi))
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 640, 60))

        text1 = help_font.render("R/G/B - color | E - erase", True, (255,255,255))
        text2 = help_font.render("1-square 2-triangle 3-eq 4-rhombus 5-circle", True, (255,255,255))
        text3 = help_font.render("Mouse: size | ESC - exit", True, (255,255,255))
        text4 = help_font.render(f"Mode: {mode}", True, (255,255,255))
        text5 = help_font.render(f"Tool: {modi}", True, (255,255,255))
        screen.blit(text1, (10, 5))
        screen.blit(text2, (10, 20))
        screen.blit(text3, (10, 35))
        screen.blit(text4, (400, 5))
        screen.blit(text5, (400, 25))
        
        for i in range(len(points) - 1):
            drawLineBetween(
                screen,
                i,
                points[i][0],
                points[i + 1][0],
                radius,
                points[i][1],
                points[i][2]
            )
        
        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode, modi):
    
    # градиент цвета
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'erase':
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] + progress * (end[0] - start[0]))
        y = int(start[1] + progress * (end[1] - start[1]))
        if modi == 'square':
            pygame.draw.rect(screen, color, (x, y, width, width))
        
        elif modi == 'circle':
            pygame.draw.circle(screen, color, (x, y), width)
        
        elif modi == 'triangle_right':
            points = [(x, y), (x + width, y), (x, y + width)]
            pygame.draw.polygon(screen, color, points)
        
        elif modi == 'triangle_eq':
            points = [
                (x, y),
                (x + width, y),
                (x + width // 2, y - width)
            ]
            pygame.draw.polygon(screen, color, points)
        elif modi == 'rhombus':
            points = [
                (x, y - width),
                (x + width, y),
                (x, y + width),
                (x - width, y)
            ]
            pygame.draw.polygon(screen, color, points)
main()