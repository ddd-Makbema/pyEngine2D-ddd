import pygame
import time
from pyEngine2D.game_object import GameObject as GO
from pyEngine2D.screen_init import ScreenInit
from pyEngine2D import null




def init_game():
	"""Inits the default game objects, e.g. origin, and the screen"""
	global timer
	global running
	global start_time
	global list_load_game_object
	global screen
	running = True
	timer = 0
	start_time = time.time()
	screen = ScreenInit(360,480, 60, 100, null, "MyGame")
	GO("collision handler", screen, null, "origin", "Collider2D.CollisionHandler")
	GO("origin", screen, null, "origin", "transform.Transform")




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

def game_loop():
	"""The main game loop that runs as the game runs. Returns when the pygame window is closed."""
	global running
	global timer
	for object in GO.INSTANCES:
		object.start()
	while running:
		for event in pygame.event.get():  
			if event.type == pygame.QUIT:
				running = False
				return
			if event.type == pygame.VIDEORESIZE:
				screen.width = screen.screen.get_size()[0]
				screen.height = screen.screen.get_size()[1]
				print([screen.width, screen.height])
		while timer > screen.fixed_fps:
			fixed_update()
			timer -= screen.fixed_fps
		update()
		screen.clock.tick(screen.fps)
		timer += delta_time()
	pygame.quit()
	return

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
