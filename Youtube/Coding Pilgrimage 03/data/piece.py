import pygame as pg
from .constants import WIDTH, HEIGHT, TILE_WIDTH	

class Piece(pg.sprite.Sprite):
	def __init__(self, type, x, y):
		pg.sprite.Sprite.__init__(self)
		self.type = type
		self.x = x
		self.y = y

		self.load_sprite()

	def load_sprite(self):
		if self.type:
			filename = "assets/X.png"
		else:
			filename = "assets/O.png"

		self.image = pg.image.load(filename)
		self.image = pg.transform.scale(self.image,(int(TILE_WIDTH), int(TILE_WIDTH)))

		self.rect = self.image.get_rect()
		self.rect.center = (TILE_WIDTH*self.x+TILE_WIDTH/2, TILE_WIDTH*self.y+TILE_WIDTH/2)