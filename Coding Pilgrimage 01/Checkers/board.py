import pygame
from .piece import Piece
from .constants import BLACK, GREY, WHITE, ROWS, COLS, TILE_WIDTH, PURPLE

class Board:
	def __init__(self):
		self.board = []
		self.selected_piece = None
		self.valid_moves = []
		self.black_pawns = self.white_pawns = 12
		self.black_kings = self.white_kings = 0

		self.setup_board()

	def draw_tiles(self, win):
		win.fill(GREY)
		for row in range(ROWS):
			for col in range(row % 2, ROWS, 2):
				pygame.draw.rect(win, WHITE, (row*TILE_WIDTH, col*TILE_WIDTH, TILE_WIDTH, TILE_WIDTH))

	def draw_pieces(self, win):
		group = pygame.sprite.Group()
		for row in self.board:
			for sprite in row:
				if sprite == 0:
					continue
				group.add(sprite)
				group.update()
		group.draw(win)

	def get_valid_moves(self):
		if self.selected_piece == None:
			self.valid_moves = []
			return

		direction = self.selected_piece.direction
		row = self.selected_piece.row
		col = self.selected_piece.col


		#print(f"direction: {direction}\ncol: {col}\nrow: {row}")

		try:
			if self.board[row+direction][col+1] == 0:
				self.valid_moves.append([row+direction, col+1])

			elif self.board[row+direction][col+1].colour != self.selected_piece.colour:
				# jump over enemy
				if self.board[row+(direction*2)][col+2] == 0:
					 self.valid_moves.append([row+(direction*2), col+2])
		except Exception:
			print("Out of bounds")

		try:
			if self.board[row+direction][col-1] == 0:
				self.valid_moves.append([row+direction, col-1])

			elif self.board[row+direction][col-1].colour != self.selected_piece.colour:
				# jump over enemy
				if self.board[row+(direction*2)][col-2] == 0:
					 self.valid_moves.append([row+(direction*2), col-2])

		except Exception:
			print("Out of bounds")


	def draw_valid_moves(self, win):
		for coord in self.valid_moves:
			pygame.draw.rect(win, PURPLE, (coord[1]*int(TILE_WIDTH), coord[0]*int(TILE_WIDTH), int(TILE_WIDTH), int(TILE_WIDTH)))


	def setup_board(self):
		for row in range(ROWS):
			self.board.append([])
			for col in range(COLS):
				if (col % 2 == ((row + 1) % 2)):
					if row < 3:
						self.board[row].append(Piece(row, col, WHITE))
					elif row >= ROWS-3:
						self.board[row].append(Piece(row, col, GREY))
					else:
						self.board[row].append(0)
				else:
					self.board[row].append(0)

	def refresh_board(self):
		board2 = [[]]

		for row in range(ROWS):
			board2.append([])
			for col in range(COLS):
				board2[row].append([])

		for row in self.board:
			for sprite in row:
				if sprite != 0:
					board2[sprite.row][sprite.col] = sprite

		for row in range(ROWS):
			for col in range(COLS):
				if board2[row][col] == []:
					board2[row][col] = 0

		self.board = board2

	def getAt(self, row, col):
		return self.board[int(row)][int(col)]


	def setAt(self, row, col, value):
		self.board[int(row)][int(col)] = value





