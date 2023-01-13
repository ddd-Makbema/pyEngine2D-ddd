import pygame
from game_object import GameObject as GO
from data_types import Vector2D
from screen_init import Init


init = Init(360,480, 100, "sam katz.jpg", "MyGame")
# GO("sam", init.screen, "sam katz.jpg", None, "player_movement.PlayerMovement", "transform.Transform" )
# GO.GAME_OBJECTS["sam"].Transform.transform = Vector2D(100,100)
# GO.GAME_OBJECTS["sam"].Transform.scale = Vector2D(2,2)
# GO.GAME_OBJECTS["sam"].Transform.rotation = 90
GO("katz", init.screen, "sam katz.jpg", "sam", "transform.Transform")
GO.GAME_OBJECTS["katz"].Transform.transform = Vector2D(100,100)
GO.GAME_OBJECTS["katz"].Transform.scale = Vector2D(2,2)
GO.GAME_OBJECTS["katz"].Transform.rotation = 90