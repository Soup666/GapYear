from .Grid import Grid
import noise

def main():
	g = Grid(15,15)
	g.generateNoise()
	g.printGrid(True)

	while True:
		print("Enter F to plant flag!\n============")
		x = input('Enter X: ')
		if x == 'F':
			x = input('Enter X: ')
			y = input('Enter Y: ')
			g.flagCoord(int(x),int(y))
			g.clearScreen(0.0)
			g.printGrid(True)
			continue
		y = input('Enter Y: ')
		g.showCoord(int(x),int(y))
		g.clearScreen(0.0)
		g.printGrid(True)

if __name__ == "__main__":
	main()