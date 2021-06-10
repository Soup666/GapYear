import pygame as pg
from .spriteSheet import SpriteSheet
from .prepare import PLAY_RECT, WIDTH, HEIGHT


class Pipe(pg.sprite.Sprite):
	def __init__(self, length, direction):
		pg.sprite.Sprite.__init__(self)
		self.length = length
		self.direction = direction

		self.x = WIDTH+50
		self.y = HEIGHT-50

		self.load_sprite()


	def update(self):
		self.rect.x -= 5

	def load_sprite(self):
		filename = "assets/sprites/spriteSheet.png"
		ss = SpriteSheet(filename)

		rect = (83, 320, 28, 160)
		multiplier = 1.2
		self.image = ss.image_at(rect)
		self.image = pg.transform.scale(self.image,(int(55*multiplier),int(self.length*multiplier)))
		
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

		if self.direction == -1:
			self.image = pg.transform.flip(self.image, False, True)
			self.y = 0
			self.rect.y = 0

	def __repr__(self):
		return f"Pipe at {self.rect.x}, {self.rect.y}"