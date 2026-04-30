import pygame

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GRAY   = (100, 100, 100)
DGRAY  = (50,  50,  50)
GREEN  = (0,   200, 0)
RED    = (200, 0,   0)
BLUE   = (0,   0,   200)
YELLOW = (255, 220, 0)

font_big   = None
font_med   = None
font_small = None

def init_fonts():
    global font_big, font_med, font_small
    font_big   = pygame.font.SysFont("Verdana", 48)
    font_med   = pygame.font.SysFont("Verdana", 28)
    font_small = pygame.font.SysFont("Verdana", 20)


# --- КНОПКА ---
class Button:
    def __init__(self, x, y, w, h, text, color=GRAY):
        self.rect  = pygame.Rect(x, y, w, h)
        self.text  = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=8)
        txt = font_med.render(self.text, True, WHITE)
        tx = self.rect.centerx - txt.get_width() // 2
        ty = self.rect.centery - txt.get_height() // 2
        surface.blit(txt, (tx, ty))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# --- ГЛАВНОЕ МЕНЮ ---
def draw_main_menu(surface, buttons):
    surface.fill(DGRAY)
    title = font_big.render("RACER", True, YELLOW)
    surface.blit(title, (surface.get_width() // 2 - title.get_width() // 2, 80))
    for btn in buttons:
        btn.draw(surface)


# --- ЭКРАН ВВОДА ИМЕНИ ---
def draw_name_screen(surface, name):
    surface.fill(DGRAY)
    t1 = font_med.render("Enter your name:", True, WHITE)
    t2 = font_big.render(name + "|", True, YELLOW)
    t3 = font_small.render("Press Enter to start", True, GRAY)
    cx = surface.get_width() // 2
    surface.blit(t1, (cx - t1.get_width() // 2, 180))
    surface.blit(t2, (cx - t2.get_width() // 2, 240))
    surface.blit(t3, (cx - t3.get_width() // 2, 320))


# --- GAME OVER ---
def draw_game_over(surface, score, distance, coins, buttons):
    surface.fill(DGRAY)
    t = font_big.render("GAME OVER", True, RED)
    surface.blit(t, (surface.get_width() // 2 - t.get_width() // 2, 60))

    lines = [
        f"Score:    {score}",
        f"Distance: {distance} m",
        f"Coins:    {coins}",
    ]
    for i, line in enumerate(lines):
        txt = font_med.render(line, True, WHITE)
        surface.blit(txt, (surface.get_width() // 2 - txt.get_width() // 2, 160 + i * 45))

    for btn in buttons:
        btn.draw(surface)


# --- LEADERBOARD ---
def draw_leaderboard(surface, lb, back_btn):
    surface.fill(DGRAY)
    t = font_big.render("TOP 10", True, YELLOW)
    surface.blit(t, (surface.get_width() // 2 - t.get_width() // 2, 30))

    header = font_small.render(f"{'#':<4} {'Name':<15} {'Score':<8} {'Distance'}", True, GRAY)
    surface.blit(header, (30, 100))
    pygame.draw.line(surface, GRAY, (30, 122), (370, 122), 1)

    for i, entry in enumerate(lb):
        line = f"{i+1:<4} {entry['name']:<15} {entry['score']:<8} {entry['distance']} m"
        color = YELLOW if i == 0 else WHITE
        txt = font_small.render(line, True, color)
        surface.blit(txt, (30, 130 + i * 30))

    back_btn.draw(surface)


# --- НАСТРОЙКИ ---
def draw_settings(surface, settings, buttons):
    surface.fill(DGRAY)
    t = font_big.render("SETTINGS", True, YELLOW)
    surface.blit(t, (surface.get_width() // 2 - t.get_width() // 2, 40))

    lines = [
        f"Sound:      {'ON' if settings['sound'] else 'OFF'}",
        f"Difficulty: {settings['difficulty'].upper()}",
        f"Car color:  {settings['car_color'].upper()}",
    ]
    for i, line in enumerate(lines):
        txt = font_med.render(line, True, WHITE)
        surface.blit(txt, (30, 130 + i * 45))

    for btn in buttons:
        btn.draw(surface)
