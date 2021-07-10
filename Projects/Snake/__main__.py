from .Snake import Snake
from .Grid import Grid
from pprint import pprint
import time

def main():
	print("Running...")
	s = Snake(5,5)
	g = Grid(15,15)

	while True:
		s.push_and_pop()
		g.clear()
		g.addSnake(s)

		pprint(g.grid)
		time.sleep(1)

if __name__ == "__main__":
	main()
