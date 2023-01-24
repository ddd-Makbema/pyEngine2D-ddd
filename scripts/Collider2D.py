import math
from game_object import GameObject
import pygame

class CollisionHandler():
    """Top level class to hold main methods and attributes for colliders. 
    Each child class will contain methods to determine if two game objects are touching."""
    ALL_COLLIDERS = []

    def fixed_update():
        for i in CollisionHandler.ALL_COLLIDERS:
            pass
        

class RectangleCollider2D():
    def __init__(self, game_object):
        self.game_object = game_object
        self.is_trigger = False
        super().__init__(self, game_object)
        self.top_left = []
        self.top_right = []
        self.bottom_left = []
        self.bottom_right = []
        CollisionHandler.ALL_COLLIDERS.append(self)
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        self.collider_size = []
        
      

    def fixed_update(self):
        if self.collider_size != self.collider_size_prev or self.collider_transform != self.collider_transform_prev:
            self.top_right = [self.collider_transform[0] + self.collider_size[0][0], self.collider_transform[1] + self.collider_size[0][1]]
            self.top_left = [self.collider_transform[0] + self.collider_size[1][0], self.collider_transform[1] + self.collider_size[1][1]]
            self.bottom_right = [self.collider_transform[0] + self.collider_size[2][0], self.collider_transform[1] + self.collider_size[2][1]]
            self.bottom_left = [self.collider_transform[0] + self.collider_size[3][0], self.collider_transform[1] + self.collider_size[3][1]]
            self.collider_transform_prev = self.collider_transform
            self.collider_size_prev = self.collider_size
  
    def get_verticies(self):
        return [self.top_right, self.top_left, self.bottom_right, self.bottom_left]
        
    def draw_collider(self, color=(0,0,0)):
        pygame.draw.line(self.game_object.screen, color, self.top_left, self.top_right)
        pygame.draw.line(self.game_object.screen, color, self.top_left, self.bottom_left)
        pygame.draw.line(self.game_object.screen, color, self.top_right, self.bottom_right)
        pygame.draw.line(self.game_object.screen, color, self.bottom_right, self.bottom_left)


    
class CircleCollider2D():
    def __init__(self, game_object):
        self.game_object = game_object
        self.is_trigger = False
        self.collider_type = ""
        super().__init__(self, game_object)
        CollisionHandler.ALL_COLLIDERS.append(self)
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        self.collider_size = [self.game_object.Transform.final_scale[0], self.game_object.Transform.final_scale[1]]
        self.scale = [1,1,1,1] #[top, bottom, right, left]
    
    def get_verticies(self):
        return [self.center]

    def fixed_update(self):
        if self.collider_size != self.collider_size_prev or self.collider_transform != self.collider_transform_prev:
            self.center = self.collider_transform
            self.collider_transform_prev = self.collider_transform
            self.collider_size_prev = self.collider_size


class SpriteColliderConvexPoly2D():
    def get_verticies(self):
        return self.verticies


'''
transform.x + 1/2 size.x = x for top 
transform.x - 1/2 size.x = x for bottom 
transform.y + 1/2 size.y = y for right
transform.y - 1/2 size.y = y for left

'''
