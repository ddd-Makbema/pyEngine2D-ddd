import pygame
from GameObject import GameObject
from dataTypes import Vector2D
from initFunc import Init
from scripts import *


init = Init(360,480,30, 100, "MyGame")
startVel = Vector2D(0,0)

listLoadGO = []

gameObject = GameObject("sam", init.screen, "sam katz.jpg", Vector2D(0,0), Vector2D(1,1) ,0, "PlayerMovement")
gameObject2 = GameObject("katz", init.screen, "sam katz.jpg")
for object in GameObject.instanceList:
	object.start()

running = True
i=0
while running:
    #1 Process input/events
	init.clock.tick(init.FPS)
	init.screen.fill(init.BLACK);
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
		init.screen.blit(object.load, (object.transform.x, object.transform.y))
		llgIt+=1
	init.FrameEnd()       
	i+=1



    ## Done after drawing everything to the screen

pygame.quit()