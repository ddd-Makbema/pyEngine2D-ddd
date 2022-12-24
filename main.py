import pygame
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init
from scripts import *

init = Init(360,480,30, 100, "sam katz.jpg", "MyGame")

list_load_game_object = []

game_object = GameObject("sam", init.screen, "sam katz.jpg", Vector2D(180,240), Vector2D(2,2) ,45, None, "player_movement.PlayerMovement" )
game_object = GameObject("katz", init.screen, "sam katz.jpg", Vector2D(50,50), Vector2D(1,1) ,0, "sam")

for object in GameObject.instances:
	object.start()

running = True
i=0
while running:
	init.clock.tick(init.fps)
	init.screen.fill(init.green)
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False

	for object in GameObject.instances:
		object.update()
	if (i%init.fixed_fps):
		for object in GameObject.instances:
			object.fixed_update()
			
	count = 0
	for object in GameObject.instances:
		object_transform = object.load.get_rect(
				center = object.parent_transform())
		init.screen.blit(object.load, object_transform)
		count+=1
	init.frame_end()       
	i+=1
pygame.quit()