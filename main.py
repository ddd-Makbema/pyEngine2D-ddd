import pygame
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init
from scripts import *

init = Init(360,480,30, 100, "sam katz.jpg", "MyGame")

list_load_game_object = []

#init all game objects
GameObject("sam", init.screen, "sam katz.jpg", Vector2D(180,240), Vector2D(2,2) ,45, None, "player_movement.PlayerMovement" )
GameObject("katz", init.screen, "sam katz.jpg", Vector2D(50,50), Vector2D(1,1) ,0, "sam")

#calls start methods for all all game objects
for object in GameObject.INSTANCES:
	object.start()

running = True
i=0
#main game loop for fps
while running:
	init.clock.tick(init.fps)
	init.screen.fill(init.green)
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False

	for object in GameObject.INSTANCES:
		object.update()
	if (i%init.fixed_fps):  #split this into seperate loop later
		for object in GameObject.INSTANCES:
			object.fixed_update()
			
	count = 0
	#loads the images onto the screen accounting for transform
	for object in GameObject.INSTANCES:
		object_transform = object.load.get_rect(
				center = object.parent_transform())
		init.screen.blit(object.load, object_transform)
		count+=1
	init.frame_end()       
	i+=1
pygame.quit()