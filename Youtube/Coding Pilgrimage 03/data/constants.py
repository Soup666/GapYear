import pygame as pg

# Constants
WIDTH, HEIGHT = 720,720
BACKGROUND_COLOR = (255,125,60)

TILE_WIDTH = WIDTH/3

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SPRITE_GROUP = pg.sprite.Group()

# Setup game
pg.init()

WIN = pg.display.set_mode((WIDTH, HEIGHT))
WIN.fill(BACKGROUND_COLOR)

pg.display.update()
