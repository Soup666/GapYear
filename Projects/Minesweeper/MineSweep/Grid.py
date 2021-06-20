from pprint import pprint
from noise import pnoise2, snoise2
import random
import os
import time as t

class Grid:
	def __init__(self, width, height):
		self.clearScreen(0.0)
		self.width = width
		self.height = height

		self.grid = []
		self.shownGrid = []

		self.setupGrid()

	def clearScreen(self, time: float):
		t.sleep(time)
		os.system('cls' if os.name == 'nt' else 'clear')

	def setupGrid(self):
		for i in range(self.height):
			self.grid.append([])
			self.shownGrid.append([])
			for j in range(self.width):
				self.grid[i].append(' ')
				self.shownGrid[i].append(' ')

	def flagCoord(self,x: int,y: int):
		self.shownGrid[y][x] = 'F'

	def printGrid(self, player: bool):
		line = '  | ' + ''.join([str(i) + "| " for i in range(9)])
		line += ''.join([str(i+9) + "|" for i in range(self.width-9)])
		print(line)
		if not player:
			for row in self.grid:
				print('| '.join([str(i) for i in row]))
			return

		j = 0
		for row in self.shownGrid:
			if j < 10:
				print(str(j) +  ' | ' + '| '.join([str(i) for i in row]))
			else:
				print(str(j) +  '| ' + '| '.join([str(i) for i in row]))
			j += 1

	def showCoord(self,x: int,y: int):
		self.shownGrid[y][x] = self.grid[y][x]

		active_nodes = []
		deactive_nodes = []

		if self.grid[y][x] != 0:
			return

		active_nodes.append([x,y])
		while len(active_nodes) > 0:
			node = active_nodes[0]
			#print("Current Node: " + str(node[0]) + ", " + str(node[1]))
			_x = node[0]
			_y = node[1]

			self.shownGrid[_y][_x] = self.grid[_y][_x]

			# Check horizontal and vertical no diagonals
			for Y in range(3):
					_Y = Y - 1


					if (y == 0 and _Y == -1) or (y == self.height-1 and _Y == 1):
						continue

					if self.grid[y+_Y][x] == 0 and [x,y+_Y] not in deactive_nodes:
						if Y == 0 or [x,y+_Y] in active_nodes:
							#print("trying: " + str(x) + ", " + str(y+_Y) + ": " + str(self.grid[y+_Y][x]))
							continue
						#print("Added: " + str(x) + "," + str(y+_Y))
						active_nodes.append([x,y+_Y])

			for X in range(3):
					_X = X - 1

					if (x == 0 and _X == -1) or (x == self.width-1 and _X == 1):
							continue

					if self.grid[y][x+_X] == 0 and [x+_X,y] not in deactive_nodes:
						if X == 0 or [x+_X,y] in active_nodes:
							continue
						#print("Added: " + str(x+_X) + "," + str(y))
						active_nodes.append([x+_X,y])


			active_nodes.remove([_x,_y])
			if [_x,_y] not in deactive_nodes:
				deactive_nodes.append([_x,_y])

			x = _x
			y = _y

			#pprint(active_nodes)
			#pprint(deactive_nodes)
			#print("==")

			self.clearScreen(0.1)
			self.printGrid(True)

	def getNeighbours(self,x: int,y: int) -> list:
		neighbours = []
		for Y in range(3):
					for X in range(3):
						_Y = Y - 1
						_X = X - 1
						if (y == _Y and x == _X) or (y == 0 and _Y == -1) or (y == self.height-1 and _Y == 1) or (x == 0 and _X == -1) or (x == self.width-1 and _X == 1):
							continue
						neighbours.append([x+_X, y+_Y])
		return neighbours


	def generateNoise(self):
		# freq 4.0 base 10
		freq = 4.0

		for y in range(self.height):
			for x in range(self.width):
				tmp = abs(round(snoise2(x / freq, y / freq, base=10), 2))

				if tmp > 0.6 or tmp < 0.1:
					self.grid[y][x] = 'B'
				else:
					self.grid[y][x] = ' '

		for y in range(self.height):
			for x in range(self.width):
				if self.grid[y][x] == 'B':
					continue

				count = 0
				for i in self.getNeighbours(x,y):
					if self.grid[i[1]][i[0]] == 'B':
							count += 1
				

				self.grid[y][x] = count




