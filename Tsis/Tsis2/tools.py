import pygame
from collections import deque

def draw_pencil(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_line(surface, start, end, color, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_rectangle(surface, start, end, color, size):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(end[0] - start[0])
    h = abs(end[1] - start[1])
    pygame.draw.rect(surface, color, (x, y, w, h), size)

def draw_circle(surface, start, end, color, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    r = int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5 // 2)
    if r > 0:
        pygame.draw.circle(surface, color, (cx, cy), r, size)

def draw_square(surface, start, end, color, size):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, color, (start[0], start[1], side, side), size)

def draw_triangle_right(surface, start, end, color, size):
    points = [start, (end[0], start[1]), (start[0], end[1])]
    pygame.draw.polygon(surface, color, points, size)

def draw_triangle_eq(surface, start, end, color, size):
    base = abs(end[0] - start[0])
    points = [
        (start[0], end[1]),
        (end[0], end[1]),
        (start[0] + base // 2, end[1] - base)
    ]
    pygame.draw.polygon(surface, color, points, size)

def draw_rhombus(surface, start, end, color, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    points = [
        (cx, start[1]),
        (end[0], cy),
        (cx, end[1]),
        (start[0], cy)
    ]
    pygame.draw.polygon(surface, color, points, size)

def flood_fill(surface, x, y, fill_color):
    target_color = surface.get_at((x, y))
    if target_color == fill_color:
        return

    width, height = surface.get_size()
    queue = deque()
    queue.append((x, y))
    visited = set()
    visited.add((x, y))

    while queue:
        cx, cy = queue.popleft()
        if surface.get_at((cx, cy)) != target_color:
            continue
        surface.set_at((cx, cy), fill_color)

        for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
