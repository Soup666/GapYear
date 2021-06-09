from .constants import WHITE, GREY, TILE_WIDTH, PADDING
import pygame

class Piece(pygame.sprite.Sprite):
	def __init__(self, row, col, colour):
		self.row = row
		self.col = col
		self.king = False
		self.sprite = ""
		self.colour = colour

		if self.colour == GREY:
			self.direction = -1
			self.sprite = "Assets/GREY.png"
		else:
			self.direction = 1
			self.sprite = "Assets/WHITE.png"

		self.x = 0
		self.y  = 0

		self.update_sprite()

	def make_king(self):
		self.king = True
		if self.colour == GREY:
			self.sprite = "Assets/GREY_KING.png"
		else:
			self.sprite = "Assets/WHITE_KING.png"
		self.direction = 0

	def move(self, row, col):
		self.row = row
		self.col = col
		self.update_sprite()

	def update_sprite(self):
		self.calc_pos()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(self.sprite)
		self.image = pygame.transform.scale(self.image, (int(TILE_WIDTH)-PADDING, int(TILE_WIDTH)-PADDING))
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

	def calc_pos(self):
		self.x = TILE_WIDTH * self.col + (TILE_WIDTH/2)
		self.y = TILE_WIDTH * self.row + (TILE_WIDTH/2)

	def __repr__(self):
		return f"S"
