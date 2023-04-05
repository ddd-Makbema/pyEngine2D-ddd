from pyEngine2D.game_object import GameObject
import pygame

class Bounce:
    def __init__(self, game_object):
        self.game_object = game_object
    def start(self):
        self.x_speed = 5
        self.y_speed = -5
    def update(self):
        if (self.game_object.Transform.transform[0] < 0 or
        self.game_object.Transform.transform[0] > self.game_object.screen.width): 
            self.x_speed = -self.x_speed
        elif (self.game_object.Transform.transform[1] < 0 or
        self.game_object.Transform.transform[1] > self.game_object.screen.height): 
            self.y_speed = -self.y_speed
        self.game_object.Transform.add_transform(self.x_speed, self.y_speed)
