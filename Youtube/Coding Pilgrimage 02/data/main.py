from . import prepare, tools

def main():
	app = tools.Control(prepare.CAPTION)
	app.main()