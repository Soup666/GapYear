import pygame as pg
import pygame as pg
from pprint import pprint
from .constants import *
from .piece import Piece

class App:
	def __init__(self, caption):
		self.run = True
		self.turn = True # True indicates X

		self.board = [  ['_', '_', '_'],
						['_', '_', '_'],
						['_', '_', '_']  ]

		self.pieces = []

	def main(self):
		while self.run:
			self.draw_grid()
			self.event_loop()

			self.draw_pieces()

			pg.display.update()

	def draw_grid(self):
		for x in range(3):
			pg.draw.rect(WIN, RED, ((WIDTH/3)*x-20, 0, 20, HEIGHT))
		for y in range(3):
			pg.draw.rect(WIN, RED, (0, (HEIGHT/3)*y-20, WIDTH, 20))

	def draw_pieces(self):
		self.pieces = []
		for x in range(3):
			for y in range(3):
				if self.board[x][y] == '_':
					continue
				elif self.board[x][y] == 'X':
					self.pieces.append(Piece(True, x, y))
				else:
					self.pieces.append(Piece(False, x, y))

		if self.check_win():
			print("Winner!\n==============")
			if not self.turn:
				print('X won')
			else:
				print('O won')
			self.run = False

		SPRITE_GROUP.empty()
		SPRITE_GROUP.add(self.pieces)

		SPRITE_GROUP.draw(WIN)
		pg.display.update()


	def event_loop(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.run = False
			if event.type == pg.MOUSEBUTTONUP:
				pos = pg.mouse.get_pos()
				x = int((pos[0]/WIDTH)*100 / 33)
				y = int((pos[1]/HEIGHT)*100 / 33)
				self.take_turn(x,y)

	def take_turn(self, x, y):
		if self.turn:
			self.board[x][y] = 'X'
		else:
			self.board[x][y] = 'O'

		if not self.check_win():
			self.turn = not self.turn

		pprint(self.board)

	def check_win(self):
		for y in range(3):
			if self.board[y][0] == self.board[y][1] and self.board[y][1] == self.board[y][2] and self.board[y][0] != '_':
				return True
		for x in range(3):
			if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x] and self.board[0][x] != '_':
				return True

		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
			return True

		if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[0][2] != '_':
			return True

		return False
