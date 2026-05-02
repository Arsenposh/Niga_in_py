import pygame
import random
import time
from pygame.locals import *
import os
folder = os.path.dirname(__file__)
os.chdir(folder)

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
RED    = (220, 50,  50)
GREEN  = (50,  200, 50)
BLUE   = (50,  50,  220)
YELLOW = (255, 220, 0)
ORANGE = (255, 140, 0)
GRAY   = (120, 120, 120)
DGRAY  = (50,  50,  50)

SCREEN_W = 400
SCREEN_H = 600

CAR_COLORS = {
    "blue":  BLUE,
    "red":   RED,
    "green": GREEN,
}

DIFFICULTY = {
    "easy":   {"speed": 4, "enemy_count": 1, "obstacle_freq": 180},
    "normal": {"speed": 5, "enemy_count": 2, "obstacle_freq": 120},
    "hard":   {"speed": 7, "enemy_count": 3, "obstacle_freq":  80},
}


class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_W // 2, 520)
        self.shield = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 20:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.right < SCREEN_W - 20:
            self.rect.x += 5

    def draw_shield(self, surface):
        if self.shield:
            pygame.draw.circle(surface, YELLOW, self.rect.center, 35, 3)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.center = (random.randint(40, SCREEN_W - 40),
                            random.randint(-300, -60))

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_H:
            self.rect.center = (random.randint(40, SCREEN_W - 40), -60)


class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self._pick_random()
        self.rect.center = (random.randint(40, SCREEN_W - 40), -30)

    def _pick_random(self):
        self.weight = random.choice([1, 2, 3])
        if self.weight == 1:
            self.image = pygame.image.load("coin.png").convert_alpha()
        elif self.weight == 2:
            self.image = pygame.image.load("coin2.png").convert_alpha()
        else:
            self.image = pygame.image.load("coin3.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_H:
            old_rect_x = random.randint(40, SCREEN_W - 40)
            self._pick_random()
            self.rect.center = (old_rect_x, -30)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.kind = random.choice(["barrier", "oil"])
        self.speed = speed
        if self.kind == "barrier":
            self.image = pygame.Surface((60, 20))
            self.image.fill((180, 0, 0))
        else:
            self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
            pygame.draw.ellipse(self.image, (30, 30, 30, 200), (0, 0, 50, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_W - 50), -40)

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_H:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    TYPES = ["nitro", "shield", "repair"]
    COLORS = {"nitro": ORANGE, "shield": BLUE, "repair": GREEN}

    def __init__(self, speed):
        super().__init__()
        self.kind = random.choice(self.TYPES)
        self.speed = speed
        self.spawn_time = time.time()

        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.COLORS[self.kind], (0, 0, 32, 32), border_radius=6)
        label = pygame.font.SysFont("Verdana", 12).render(self.kind[0].upper(), True, WHITE)
        self.image.blit(label, (10, 8))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_W - 40), -40)

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_H or time.time() - self.spawn_time > 8:
            self.kill()


def run_game(surface, settings, username):
    clock = pygame.time.Clock()
    font  = pygame.font.SysFont("Verdana", 18)

    diff     = DIFFICULTY[settings["difficulty"]]
    speed    = diff["speed"]
    obs_freq = diff["obstacle_freq"]

    try:
        background = pygame.image.load("AnimatedStreet.png").convert()
    except:
        background = pygame.Surface((SCREEN_W, SCREEN_H))
        background.fill((60, 60, 60))
    bg_y = 0

    car_color = CAR_COLORS[settings["car_color"]]
    player = Player(car_color)

    enemies   = pygame.sprite.Group()
    coins_grp = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups  = pygame.sprite.Group()

    for _ in range(diff["enemy_count"]):
        enemies.add(Enemy(speed))
    for _ in range(2):
        coins_grp.add(Coin(speed))

    score    = 0
    coins    = 0
    distance = 0
    frame    = 0
    lvl_step = 5
    active_powerup = None
    powerup_end    = 0
    nitro_active   = False
    shield_active  = False

    running = True
    while running:
        clock.tick(60)
        frame    += 1
        distance += 1
        score    += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                return None
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return None

        bg_y += speed
        if bg_y >= SCREEN_H:
            bg_y = 0
        surface.blit(background, (0, bg_y - SCREEN_H))
        surface.blit(background, (0, bg_y))

        player.move()
        for e in enemies:   e.move()
        for c in coins_grp: c.move()
        for o in obstacles: o.move()
        for p in powerups:  p.move()

        if frame % obs_freq == 0:
            obstacles.add(Obstacle(speed))

        if frame % 600 == 0 and len(powerups) == 0:
            powerups.add(PowerUp(speed))

        hit_coins = pygame.sprite.spritecollide(player, coins_grp, False)
        for coin in hit_coins:
            coins += coin.weight
            score += coin.weight * 10
            coin.rect.center = (random.randint(40, SCREEN_W - 40), -30)
            if coins % lvl_step == 0:
                speed += 1

        hit_pu = pygame.sprite.spritecollide(player, powerups, True)
        for pu in hit_pu:
            active_powerup = pu.kind
            if pu.kind == "nitro":
                nitro_active = True
                speed += 3
                powerup_end = time.time() + 4
            elif pu.kind == "shield":
                shield_active = True
                player.shield = True
                powerup_end = 0
            elif pu.kind == "repair":
                obstacles.empty()
                active_powerup = None

        if active_powerup == "nitro" and powerup_end > 0 and time.time() > powerup_end:
            speed = max(diff["speed"], speed - 3)
            nitro_active   = False
            active_powerup = None

        if pygame.sprite.spritecollideany(player, enemies):
            if shield_active:
                shield_active  = False
                player.shield  = False
                active_powerup = None
                enemies.empty()
                for _ in range(diff["enemy_count"]):
                    enemies.add(Enemy(speed))
            else:
                if settings["sound"]:
                    try:
                        pygame.mixer.Sound("crash.wav").play()
                        time.sleep(0.4)
                    except:
                        pass
                return {"score": score, "distance": distance // 60, "coins": coins}

        if pygame.sprite.spritecollideany(player, obstacles):
            if shield_active:
                shield_active  = False
                player.shield  = False
                active_powerup = None
                obstacles.empty()
            else:
                return {"score": score, "distance": distance // 60, "coins": coins}

        for grp in [enemies, coins_grp, obstacles, powerups]:
            grp.draw(surface)
        surface.blit(player.image, player.rect)
        player.draw_shield(surface)

        surface.blit(font.render(f"Score: {score}",          True, WHITE),  (10, 10))
        surface.blit(font.render(f"Coins: {coins}",          True, YELLOW), (10, 32))
        surface.blit(font.render(f"Dist:  {distance // 60}m",True, WHITE),  (10, 54))

        if active_powerup:
            if active_powerup == "nitro":
                remaining = max(0, int(powerup_end - time.time()))
                pu_text = f"NITRO {remaining}s"
            elif active_powerup == "shield":
                pu_text = "SHIELD"
            else:
                pu_text = active_powerup.upper()
            surface.blit(font.render(pu_text, True, ORANGE), (SCREEN_W - 120, 10))

        pygame.display.flip()

    return {"score": score, "distance": distance // 60, "coins": coins}