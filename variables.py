import pygame
from game_object import GameObject as GO
from data_types import Vector2D
from screen_init import ScreenInit



screen = ScreenInit(360,480, 60, 100, "sam katz.jpg", "MyGame")
GO("origin", screen.screen, "null.png", "origin", "transform.Transform")

GO("sam", screen.screen, "sam katz.jpg", "origin", "player_movement.PlayerMovement", "transform.Transform" )
GO.GAME_OBJECTS["sam"].Transform.transform = Vector2D(200,200)
GO.GAME_OBJECTS["sam"].Transform.scale = Vector2D(1,1)
GO.GAME_OBJECTS["sam"].Transform.rotation = 0
GO("katz", screen.screen, "sam katz.jpg", "sam", "transform.Transform")
GO.GAME_OBJECTS["katz"].Transform.transform = Vector2D(100,100)
GO.GAME_OBJECTS["katz"].Transform.scale = Vector2D(2,2)
GO.GAME_OBJECTS["katz"].Transform.rotation = 0

if __name__ == '__main__':
    pass