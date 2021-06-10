import pygame as pg
from .app import App

def main():
	app = App("TikTakToe")
	app.main()
	pg.quit()