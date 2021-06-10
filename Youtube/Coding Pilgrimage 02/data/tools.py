import pygame as pg

TIME_PER_UPDATE = 16.0  #Milliseconds

class Control(object):
	def __init__(self, caption):
		self.done = False
		self.screen = pg.display.get_surface()
		self.caption = caption
		self.clock = pg.time.Clock()
		self.fps = 60.0
		self.fps_visible = True

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

	def draw(self, interpolate):
		self.show_fps()
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