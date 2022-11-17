import pygame

class Init:
	def __init__(self, WIDTH, HEIGHT, FPS, fFps, Name_Window="<Your_Game>"):
		self.WIDTH = WIDTH
		self.Height = HEIGHT
		self.FPS = FPS
		self.FixedFps = fFps
		self.Name_Window = Name_Window
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		
		pygame.init()
		pygame.mixer.init()  ## For sound
		self.screen = pygame.display.set_mode((self.WIDTH, self.Height))
		pygame.display.set_caption(self.Name_Window)
		self.clock = pygame.time.Clock() 

	def FrameEnd(self):
		pygame.display.flip()
	def Group(self):
		return pygame.sprite.Group()