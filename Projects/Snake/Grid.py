from .Snake import Snake

class Grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.grid = []
		for y in range(self.height):
			self.grid.append([])
			for x in range(self.width):
				self.grid[y].append('_')

	
	def clear(self):
		self.grid = []
		for y in range(self.height):
			self.grid.append([])
			for x in range(self.width):
				self.grid[y].append('_')

	def addSnake(self, Snake):
		print(Snake.head[0])
		self.grid[Snake.head[0]][Snake.head[1]] = 'H'
		for section in Snake.body:
			print(section)
			self.grid[section[0]][section[1]] = 'B'
