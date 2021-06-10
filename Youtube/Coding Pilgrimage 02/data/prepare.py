import pygame as pg
import os

pg.init()

SCREEN_SIZE = (600, 600)
CAPTION = "Flappy Bird"
COLOR_KEY = (255, 0, 255)
BACKGROUND_COLOR = (30, 40, 50)
SCREEN_RECT = pg.Rect((0,0), SCREEN_SIZE)
_FONT_PATH = os.path.join("assets", "fonts","Caramel Sweets.ttf")
BIG_FONT = pg.font.Font(_FONT_PATH, 100)

pg.display.set_caption(CAPTION)
_screen = pg.display.set_mode(SCREEN_SIZE)

_screen.fill(BACKGROUND_COLOR)
_render = BIG_FONT.render("LOADING...", 0, pg.Color("white"))
_screen.blit(_render, _render.get_rect(center=SCREEN_RECT.center))
pg.display.update()