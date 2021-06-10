import pygame as pg
from .spriteSheet import SpriteSheet
from .prepare import HEIGHT, GRAVITY

class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.x = 50
		self.y = HEIGHT/2
		self.acceleration = 5

		self.load_sprite()

	def update(self):
		self.rect.y += self.acceleration
		if self.acceleration < 50:
			self.acceleration += GRAVITY

	def load_sprite(self):
		filename = "assets/sprites/spriteSheet.png"
		ss = SpriteSheet(filename)

		rect = (0, 490, 22, 15)
		self.image = ss.image_at(rect)
		self.image = pg.transform.scale(self.image,(100,75))

		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)