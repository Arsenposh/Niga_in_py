import pygame
import sys
from datetime import datetime
from tools import (
    draw_pencil, draw_line, draw_rectangle, draw_circle,
    draw_square, draw_triangle_right, draw_triangle_eq,
    draw_rhombus, flood_fill
)

WIDTH, HEIGHT = 900, 620
TOOLBAR_H = 60
CANVAS_H = HEIGHT - TOOLBAR_H

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GRAY   = (50,  50,  50)
LGRAY  = (180, 180, 180)
COLORS = [
    (0,   0,   0),    # чёрный
    (255, 255, 255),  # белый
    (255, 0,   0),    # красный
    (0,   200, 0),    # зелёный
    (0,   0,   255),  # синий
    (255, 255, 0),    # жёлтый
    (255, 165, 0),    # оранжевый
    (150, 0,   200),  # фиолетовый
    (0,   200, 200),  # голубой
    (139, 69,  19),   # коричневый
]
SIZES = [2, 5, 10]
TOOLS = ['pencil', 'line', 'rect', 'circle', 'square',
         'tri_right', 'tri_eq', 'rhombus', 'fill', 'text', 'eraser']


def draw_toolbar(screen, font, tool, color, size_idx):
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_H))
    tool_labels = {
        'pencil':    'Pencil',
        'line':      'Line',
        'rect':      'Rect',
        'circle':    'Circle',
        'square':    'Square',
        'tri_right': 'TriR',
        'tri_eq':    'TriE',
        'rhombus':   'Rhomb',
        'fill':      'Fill',
        'text':      'Text',
        'eraser':    'Eraser',
    }

    x = 5
    for t, label in tool_labels.items():
        bg = (100, 100, 200) if t == tool else (80, 80, 80)
        pygame.draw.rect(screen, bg, (x, 5, 50, 22))
        txt = font.render(label, True, WHITE)
        screen.blit(txt, (x + 3, 8))
        x += 53
    size_x = 5
    for i, s in enumerate(SIZES):
        bg = (200, 150, 50) if i == size_idx else (80, 80, 80)
        pygame.draw.rect(screen, bg, (size_x, 32, 30, 22))
        lbl = font.render(f"S{i+1}", True, WHITE)
        screen.blit(lbl, (size_x + 5, 35))
        size_x += 33
    cx = 110
    for c in COLORS:
        pygame.draw.rect(screen, c, (cx, 32, 22, 22))
        if c == color:
            pygame.draw.rect(screen, WHITE, (cx, 32, 22, 22), 2)
        cx += 25
    pygame.draw.rect(screen, color, (WIDTH - 50, 10, 40, 40))
    pygame.draw.rect(screen, WHITE, (WIDTH - 50, 10, 40, 40), 2)
    hint = font.render("Ctrl+S: Save | 1/2/3: Size | ESC: exit", True, LGRAY)
    screen.blit(hint, (WIDTH - 280, 47))


def get_toolbar_click(mx, my, tool, color, size_idx):
    """Обрабатывает клик по тулбару, возвращает новые tool, color, size_idx"""
    tool_labels = ['pencil', 'line', 'rect', 'circle', 'square',
                   'tri_right', 'tri_eq', 'rhombus', 'fill', 'text', 'eraser']
    x = 5
    for t in tool_labels:
        if x <= mx <= x + 50 and 5 <= my <= 27:
            tool = t
        x += 53
    sx = 5
    for i in range(3):
        if sx <= mx <= sx + 30 and 32 <= my <= 54:
            size_idx = i
        sx += 33
    cx = 110
    for c in COLORS:
        if cx <= mx <= cx + 22 and 32 <= my <= 54:
            color = c
        cx += 25

    return tool, color, size_idx


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint — TSIS2")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 13)
    text_font = pygame.font.SysFont("Arial", 24)
    canvas = pygame.Surface((WIDTH, CANVAS_H))
    canvas.fill(WHITE)
    tool      = 'pencil'
    color     = BLACK
    size_idx  = 0          # индекс в SIZES
    drawing   = False
    start_pos = None
    prev_pos  = None
    preview_canvas = None
    text_mode    = False
    text_pos     = None
    text_input   = ""

    running = True
    while running:
        size = SIZES[size_idx]
        pressed = pygame.key.get_pressed()
        ctrl    = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    if text_mode:
                        text_mode  = False
                        text_input = ""
                    else:
                        running = False
                if event.key == pygame.K_s and ctrl:
                    filename = "canvas_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
                    pygame.image.save(canvas, filename)
                    pygame.display.set_caption(f"Saved: {filename}")
                if event.key == pygame.K_1: size_idx = 0
                if event.key == pygame.K_2: size_idx = 1
                if event.key == pygame.K_3: size_idx = 2

                if text_mode:
                    if event.key == pygame.K_RETURN:
                        surf = text_font.render(text_input, True, color)
                        canvas.blit(surf, text_pos)
                        text_mode  = False
                        text_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        if event.unicode and event.unicode.isprintable():
                            text_input += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                if my < TOOLBAR_H:
                    tool, color, size_idx = get_toolbar_click(mx, my, tool, color, size_idx)
                    continue

                cy = my - TOOLBAR_H  # координата на canvas

                if tool == 'fill':
                    flood_fill(canvas, mx, cy, color + (255,))

                elif tool == 'text':
                    text_mode  = True
                    text_pos   = (mx, cy)
                    text_input = ""

                else:
                    drawing   = True
                    start_pos = (mx, cy)
                    prev_pos  = (mx, cy)
                    if tool == 'line':
                        preview_canvas = canvas.copy()
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    mx, my = event.pos
                    cy = my - TOOLBAR_H
                    cur_pos = (mx, cy)

                    if tool == 'pencil':
                        draw_pencil(canvas, prev_pos, cur_pos, color, size)
                        prev_pos = cur_pos

                    elif tool == 'eraser':
                        draw_pencil(canvas, prev_pos, cur_pos, WHITE, size * 4)
                        prev_pos = cur_pos

                    elif tool == 'line':
                        canvas.blit(preview_canvas, (0, 0))
                        draw_line(canvas, start_pos, cur_pos, color, size)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing:
                    mx, my = event.pos
                    cy = my - TOOLBAR_H
                    end_pos = (mx, cy)

                    if tool == 'line':
                        canvas.blit(preview_canvas, (0, 0))
                        draw_line(canvas, start_pos, end_pos, color, size)

                    elif tool == 'rect':
                        draw_rectangle(canvas, start_pos, end_pos, color, size)

                    elif tool == 'circle':
                        draw_circle(canvas, start_pos, end_pos, color, size)

                    elif tool == 'square':
                        draw_square(canvas, start_pos, end_pos, color, size)

                    elif tool == 'tri_right':
                        draw_triangle_right(canvas, start_pos, end_pos, color, size)

                    elif tool == 'tri_eq':
                        draw_triangle_eq(canvas, start_pos, end_pos, color, size)

                    elif tool == 'rhombus':
                        draw_rhombus(canvas, start_pos, end_pos, color, size)

                    drawing = False
                    start_pos = None
                    preview_canvas = None
        screen.fill(GRAY)
        screen.blit(canvas, (0, TOOLBAR_H))
        draw_toolbar(screen, font, tool, color, size_idx)

        if text_mode and text_pos:
            preview = text_font.render(text_input + "|", True, color)
            screen.blit(preview, (text_pos[0], text_pos[1] + TOOLBAR_H))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


main()
