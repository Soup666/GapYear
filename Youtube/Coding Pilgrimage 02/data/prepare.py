import pygame as pg
import random
import os

pg.init()

WIDTH, HEIGHT = 600, 600

SCREEN_SIZE = (WIDTH, HEIGHT)
PLAY_RECT = pg.Rect(0,0,WIDTH,HEIGHT)
CAPTION = "Flappy Bird"
BACKGROUND_COLOR = (255,255,255)
SCREEN_RECT = pg.Rect((0,0), SCREEN_SIZE)
_FONT_PATH = os.path.join("assets", "fonts","Caramel Sweets.ttf")
BIG_FONT = pg.font.Font(_FONT_PATH, 100)

pg.time.set_timer(pg.USEREVENT, random.randrange(1000, 1500))

pg.display.set_caption(CAPTION)
WIN = pg.display.set_mode(SCREEN_SIZE)

WIN.fill(BACKGROUND_COLOR)
pg.display.update()

SPRITE_GROUP = pg.sprite.Group()
PIPE_GROUP = pg.sprite.Group()

GRAVITY = 0.98
