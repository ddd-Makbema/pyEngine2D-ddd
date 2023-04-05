import pygame

class ScreenInit:
	"""Starts the screen for the game and initializes default values.
	
		Attributes:
			width: int of the screen width in pixels
			height: int of the screen height in pixels
			fps: int how many frames per second are shown
			fixed_fps: int seperate clock from fps used for physics calculations usually faster than fps
			name_window: string of what the screen window will show
			all color vars: tuple of 3 numbers for rgb
			start_velocity: Vector2D for an initial velocity of 0 speed
			icon: string for name of image to load on the window"""
	def __init__(self, width, height, fps, ffps, icon, name_window="<Your_Game>"):
		self.width = width
		self.height = height
		self.fixed_fps = 1/ffps
		self.fps = fps
		self.name_window = name_window
		self.white = (255, 255, 255)
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.start_velocity = [0,0]
		self.icon = icon
		
		pygame.init()
		pygame.mixer.init()  ## For sound
		pygame.display.set_caption(self.name_window)

		if self.icon:
			pygame_icon = pygame.image.load(self.icon)
			pygame.display.set_icon(pygame_icon)

		self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock() 

	def frame_end(self):
		"""Updates the screen for the new frame"""
		pygame.display.flip()

if __name__ == '__main__':
    pass