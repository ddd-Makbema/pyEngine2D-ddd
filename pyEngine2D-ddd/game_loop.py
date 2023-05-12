import pygame
import time
from pyEngine2D_ddd.game_object import GameObject as GO
from pyEngine2D_ddd.screen_init import ScreenInit
from pyEngine2D_ddd.data_load import DataLoad
from pyEngine2D_ddd import null



class GameLoop():
	def init_game(self, new_game_objects):
		"""Inits the default game objects, e.g. origin, and the screen"""
		global timer
		global running
		global start_time
		global screen
		global data_handler
		running = True
		self.is_game_objects_changed = False
		timer = 0
		start_time = time.time()
		screen = ScreenInit(360,480, 60, 100, null, "MyGame")
		GO("collision handler", screen, null, "origin", "Default", "Default", "Collider2D.CollisionHandler")
		GO("origin", screen, null, "origin", "Default", "Default", "transform.Transform")
		data_handler = DataLoad(self)
		if new_game_objects:
			data_handler.save_game_objects()
			self.is_game_objects_changed = True
		else:
			info = data_handler.import_game_object_data()
			data_handler.instantiate_game_object(info, screen)

	def game_loop(self, change_rendering_order = False):
		"""The main game loop that runs as the game runs. Returns when the pygame window is closed."""
		global running
		global timer
		data_handler.save_game_objects()
		if change_rendering_order or self.is_game_objects_changed:
			GO.new_game_object()
		else:
			GO.old_game_object()


		while running:
			for event in pygame.event.get():  
				if event.type == pygame.QUIT:
					running = False
					return
				if event.type == pygame.VIDEORESIZE:
					screen.width = screen.screen.get_size()[0]
					screen.height = screen.screen.get_size()[1]
			while timer > screen.fixed_fps:
				fixed_update()
				timer -= screen.fixed_fps
			update()
			screen.clock.tick(screen.fps)
			timer += delta_time()
		pygame.quit()
		return

	def game_objects_changed(self, changed):
		self.is_game_objects_changed = changed

def update():
	"""Renders the screen fps times a second."""
	screen.screen.fill(screen.green)
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.VIDEORESIZE:
			screen.width = screen.screen.get_size()[0]
			screen.height = screen.screen.get_size()[1]
			print([screen.width, screen.height])
	for object in GO.INSTANCES:
		object.update()			
	#loads the images onto the screen accounting for transform
	for object in GO.INSTANCES:
		try:
			object_transform = object.Transform.load.get_rect(
				center = object.Transform.parent_transform())
			screen.screen.blit(object.Transform.load, object_transform)
		except AttributeError as e:
			if "no attribute 'Transform'" not in str(e):
				raise e
			else:
				center = [-1,-1]
				screen.screen.blit(object.image_start, center)
	screen.frame_end()  

def fixed_update():
	"""calls the fixed update function at set times per second. Independent from update"""
	for object in GO.INSTANCES:
		object.fixed_update()

def delta_time():
	global start_time
	x = time.time() - start_time
	start_time = time.time()
	return x


def quit():
	pygame.quit


if __name__ == '__main__':
    pass

# All Awake calls
# All Start Calls
# while (stepping towards variable delta time)
# All FixedUpdate functions
# Physics simulation
# OnEnter/Exit/Stay trigger functions
# OnEnter/Exit/Stay collision functions
# Rigidbody interpolation applies transform.position and rotation
# OnMouseDown/OnMouseUp etc. events
# All Update functions

# GO("sam", screen, "null.png", "origin", "transform.Transform", "Collider2D.RectangleCollider2D", "player_movement.PlayerMovement")
# GO.GAME_OBJECTS["sam"].RectangleCollider2D.set_collider_size([20,20])
# GO.GAME_OBJECTS["sam"].Transform.transform = [220,220]
# GO.GAME_OBJECTS["sam"].Transform.scale = [1,1]
# GO.GAME_OBJECTS["sam"].Transform.rotation = 0

# GO("katz", screen, "null.png", "origin", "transform.Transform", "Collider2D.RectangleCollider2D", "player_movement.PlayerMovement")
# GO.GAME_OBJECTS["katz"].RectangleCollider2D.set_collider_size([20,20])
# GO.GAME_OBJECTS["katz"].Transform.transform = [300,250]
# GO.GAME_OBJECTS["katz"].Transform.scale = [1,1]
# GO.GAME_OBJECTS["katz"].Transform.rotation = 0
