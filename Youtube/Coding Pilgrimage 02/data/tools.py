import pygame as pg
from .pipe import Pipe
from .player import Player
from .prepare import SPRITE_GROUP, WIN, BACKGROUND_COLOR, HEIGHT, PIPE_GROUP
import random

TIME_PER_UPDATE = 16.0  #Milliseconds

class Control(object):
	def __init__(self, caption):
		self.done = False
		self.screen = pg.display.get_surface()
		self.caption = caption
		self.clock = pg.time.Clock()
		self.fps = 60.0
		self.fps_visible = True

		self.player = Player()
		self.pipes = []
		self.score = 0

		self.spawn_objects()
		
	def spawn_objects(self):
		# Player

		SPRITE_GROUP.add(self.pipes)
		SPRITE_GROUP.add(self.player)


	def main(self):
		lag = 0.0
		while not self.done:
			lag += self.clock.tick(self.fps)
			self.event_loop()
			while lag >= TIME_PER_UPDATE:
				self.update()
				lag -= TIME_PER_UPDATE
			self.draw(lag/TIME_PER_UPDATE)

	def update(self):
		self.now = pg.time.get_ticks()

		self.player.update()

		for i in range(len(self.pipes)-1):
			self.pipes[i].update()

			if self.pipes[i].rect.x < -50:
				SPRITE_GROUP.remove(self.pipes[i])
				self.pipes.pop(i)

		col = pg.sprite.spritecollide(self.player, PIPE_GROUP, True)
		if len(col) > 0:
			print(col)
			self.done = True
			print("Failed!")

	def draw(self, interpolate):
		#WIN.fill(BACKGROUND_COLOR)
		self.show_fps()

		SPRITE_GROUP.draw(WIN)
		pg.display.update()

	def show_fps(self):
		"""
		Display the current FPS in the window handle if fps_visible is True.
		"""
		if self.fps_visible:
			fps = self.clock.get_fps()
			with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
			pg.display.set_caption(with_fps)

	def event_loop(self):
		"""
		Process all events and pass them down to the state_machine.
		The f5 key globally turns on/off the display of FPS in the caption
		"""
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.done = True
			if event.type == pg.KEYDOWN:
				self.player.acceleration = -15
				#self.player.rect.y -= 120
			if event.type == pg.USEREVENT:
				self.score += 1
				print(f"Score: {self.score}")
				d = random.randint(0,100)
				if d > 50:
					dir = 1
				else:
					dir = -1
				p = Pipe(random.randint(100,HEIGHT/2), dir)
				self.pipes.append(p)
				SPRITE_GROUP.add(p)
				PIPE_GROUP.add(p)
