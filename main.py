import pygame
import time
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init
from variables import *

running = True
timer = 0
start_time = time.time()


list_load_game_object = []

#init all game objects




def update():
	"""Renders the screen fps times a second."""
	init.screen.fill(init.green)
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False
	for object in GameObject.INSTANCES:
		object.update()			
	#loads the images onto the screen accounting for transform
	for object in GameObject.INSTANCES:
		try:
			object_transform = object.Transform.load.get_rect(
				center = object.Transform.parent_transform())
			
			init.screen.blit(object.Transform.load, object_transform)
		except AttributeError:
			pass
	init.frame_end()  

def fixed_update():
	"""calls the fixed update function at set times per second. Independent from update"""
	for object in GameObject.INSTANCES:
		object.fixed_update()

def delta_time():
	global start_time
	x = time.time() - start_time
	start_time = time.time()
	return x

while running:
	while timer > init.fixed_fps:
		fixed_update()
		timer -= init.fixed_fps
	update()
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False
	timer += delta_time()


pygame.quit()

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