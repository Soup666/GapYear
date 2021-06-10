#!/usr/bin/env python3

import pygame
from Checkers import *
from pprint import pprint
import math

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption("Checkers")

white = 0
grey = 0

def main():
	turn = True
	run = True
	clock = pygame.time.Clock()
	board = Board()

	while run:
		clock.tick(FPS)
		board.draw_tiles(WIN) # Draw Board
		board.draw_pieces(WIN) # Draw Pieces

		for event in pygame.event.get():
			moving = False
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONUP:

				pos = pygame.mouse.get_pos()

				clicked_sprites = [sprite for row in board.board for sprite in row if sprite != 0 and sprite.rect.collidepoint(pos)]
				if len(clicked_sprites) == 0:
					# Moving

					if board.selected_piece == None:
						continue
					currentPos = [board.selected_piece.row, board.selected_piece.col]

					x = math.floor(pos[0]/TILE_WIDTH)
					y = math.floor(pos[1]/TILE_WIDTH)

					coords = [y,x]

					if coords in board.valid_moves:
						# make the move
						board.board[board.selected_piece.row][board.selected_piece.col].move(coords[0], coords[1])
						#print(board.board[coords[0]][coords[1]])

						board.refresh_board()
						#pprint(board.board)

						# check for jumps
						midpoint = [(currentPos[0] + coords[0]) / 2, (currentPos[1] + coords[1]) / 2]
						magnitude = abs(currentPos[0] - coords[0]) + abs(currentPos[1] - coords[1])
						if magnitude > 2:
							if board.getAt(midpoint[0], midpoint[1]) != 0:
								colour = board.getAt(midpoint[0], midpoint[1]).colour
								if colour == GREY:
									global white
									white = white + 1
									print(f"Grey team lost a piece: {white} points to white team!")
								else:
									global grey
									grey = grey + 1
									print(f"White team lost a piece: {grey} points to grey team!")
								board.setAt(midpoint[0], midpoint[1], 0) 


					board.selected_piece = None
					board.valid_moves = []
				else:
					# clicked on a sprite

					# reset moves
					board.valid_moves = []

					col = clicked_sprites[0].col
					row = clicked_sprites[0].row

					board.selected_piece = board.board[row][col]

					board.get_valid_moves()
				    
		board.draw_valid_moves(WIN)

		pygame.display.update()

	pygame.quit()

main()