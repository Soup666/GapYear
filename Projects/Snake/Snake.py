
class Snake:
	def __init__(self, x, y):
		self.head = [x,y]
		self.body = []

		self.direction = "UP"

	def push_and_pop(self):
		self.body.append(self.head)
		if self.direction == "UP":
			self.head = [self.head[0], self.head[1]+1]
		elif self.direction == "DOWN":
			self.head = [self.head[0], self.head[1]-1]
		elif self.direction == "LEFT":
			self.head = [self.head[0]-1, self.head[1]]
		elif self.direction == "RIGHT":
			self.head = [self.head[0]+1, self.head[1]]
		if len(self.body) > 5:
			self.body.pop(0)

		