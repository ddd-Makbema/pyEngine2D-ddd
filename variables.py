import pygame
from game_object import GameObject
from data_types import Vector2D
from screen_init import Init


init = Init(360,480, 100, "sam katz.jpg", "MyGame")
GameObject("sam", init.screen, "sam katz.jpg", None, "player_movement.PlayerMovement" )
print(GameObject.GAME_OBJECTS["sam"].PlayerMovement)
GameObject("katz", init.screen, "sam katz.jpg", "sam")