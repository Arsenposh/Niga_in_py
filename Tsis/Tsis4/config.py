WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_RED = (139, 0, 0)
BLUE = (0, 100, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
CYAN = (0, 255, 255)

FOOD_COLORS = {
    1: (255, 0, 0),
    2: (255, 255, 0),
    3: (255, 255, 255)
}


FOOD_SIZE = CELL_SIZE
FOOD_LIFETIME = 5000  


POISON_COLOR = DARK_RED


POWERUP_LIFETIME = 8000  
POWERUP_EFFECT_DURATION = 5000  

POWERUP_COLORS = {
    "speed_boost": ORANGE,
    "slow_motion": CYAN,
    "shield": PURPLE
}


START_SPEED = 8


OBSTACLE_START_LEVEL = 3
OBSTACLE_COUNT_PER_LEVEL = 3  


DB_CONFIG = {
    "host": "localhost",
    "database": "snake_game",
    "user": "postgres",
    "password": "12345678",
    "port": 5432
}
