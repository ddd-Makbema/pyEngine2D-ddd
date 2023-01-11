import pygame
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init


init = Init(360,480, 100, "sam katz.jpg", "MyGame")
GameObject("sam", init.screen, "sam katz.jpg", Vector2D(180,240), Vector2D(2,2) ,45, None, "player_movement.PlayerMovement" )
GameObject("katz", init.screen, "sam katz.jpg", Vector2D(50,50), Vector2D(1,1) ,0, "sam")