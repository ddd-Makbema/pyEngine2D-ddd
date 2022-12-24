import pygame

class Init:
	def __init__(self, width, height, fps, ffps, icon, name_window="<Your_Game>"):
		self.width = width
		self.height = height
		self.fps = fps
		self.fixed_fps = ffps
		self.name_window = name_window
		self.white = (255, 255, 255)
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.blue = (0, 0, 255)
		self.start_velocity = Vector2D(0,0)
		self.icon = icon
		
		pygame.init()
		pygame.mixer.init()  ## For sound
		pygame.display.set_caption(self.name_window)
		if self.icon:
			pygame_icon = pygame.image.load("data/" + self.icon)
			pygame.display.set_icon(pygame_icon)
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock() 

	def frame_end(self):
		pygame.display.flip()
	def group(self):
		return pygame.sprite.Group()