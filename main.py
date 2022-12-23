import pygame
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init
from scripts import *

init = Init(360,480,30, 100, "sam katz.jpg", "MyGame")
startVel = Vector2D(0,0)

listLoadGO = []

gameObject = GameObject("sam", init.screen, "sam katz.jpg", Vector2D(180,240), Vector2D(2,2) ,45, None, "player_movement.PlayerMovement" )
gameObject = GameObject("katz", init.screen, "sam katz.jpg", Vector2D(50,50), Vector2D(1,1) ,0, "sam")

for object in GameObject.instanceList:
	object.start()

running = True
i=0
while running:
    #1 Process input/events
	init.clock.tick(init.FPS)
	init.screen.fill(init.GREEN)
	for event in pygame.event.get():   
		if event.type == pygame.QUIT:
			running = False
    #3 Draw/render

	for object in GameObject.instanceList:
		object.Update()
	if (i%init.FixedFps):
		for object in GameObject.instanceList:
			object.FixedUpdate()
			
	llgIt = 0
	for object in GameObject.instanceList:
		objectTransform = object.load.get_rect(
				center = object.ParentTransform())
		init.screen.blit(object.load, objectTransform)
		llgIt+=1
	init.FrameEnd()       
	i+=1
pygame.quit()