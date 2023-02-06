from game_object import GameObject
from itertools import combinations
import math
import pygame

class CollisionHandler():
    """Top level class to hold main methods and attributes for colliders. 
    Each child class will contain methods to determine if two game objects are touching."""
    ALL_COLLIDERS = []
    def __init__(self, game_object):
        self.prev_colliders = ["a", "b", "c"]
    def start(self):
        self.colliderPairs = list(combinations(CollisionHandler.ALL_COLLIDERS, 2))

    def fixed_update(self):
        if CollisionHandler.ALL_COLLIDERS != self.prev_colliders:
            self.colliderPairs = list(combinations(CollisionHandler.ALL_COLLIDERS, 2))
            self.prev_colliders = CollisionHandler.ALL_COLLIDERS
            print(self.colliderPairs)
        
        for i in self.colliderPairs:
            line = [i[0].collider_transform, i[1].collider_transform]
            



class RectangleCollider2D():
    def __init__(self, game_object):
        self.game_object = game_object
        self.is_trigger = False
        self.top_left = []
        self.top_right = []
        self.bottom_left = []
        self.bottom_right = []
        CollisionHandler.ALL_COLLIDERS.append(self)
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        self.collider_transform_prev = [0,0]
        self.collider_size = [0,0]
        self.collider_size_prev = [-1,-1]
        self.collider_size_orig = [0,0]
        self.rotation_prev = 1000
        self.prev_t_scale = [-1,-1]
        self.axis_amount = 2

    def start(self):
        self.fixed_update()

    def _is_update(self):
        if self.collider_size == self.collider_size_prev:
            if self.collider_transform == self.collider_transform_prev:
                if self.game_object.Transform.scale == self.prev_t_scale:
                    if self.rotation_prev == self.game_object.Transform.rotation:   
                        return False
        return True  

    def fixed_update(self):
        self.collider_transform = [self.game_object.Transform.transform[0], self.game_object.Transform.transform[1]]
        if self._is_update():
            self.collider_size[0] = self.collider_size_orig[0] * self.game_object.Transform.scale[0]
            self.collider_size[1] = self.collider_size_orig[1] * self.game_object.Transform.scale[1]
           
            self.collider_transform_prev = self.collider_transform
            self.collider_size_prev = self.collider_size
            self.prev_t_scale = self.game_object.Transform.scale
            self.rotation_prev = self.game_object.Transform.rotation
  
    def get_verticies(self):
        return [self.top_right, self.top_left, self.bottom_right, self.bottom_left]
        
    def draw_collider(self, color=(0,0,0)):
        collider = pygame.Surface(self.collider_size).convert_alpha()
        collider = pygame.transform.rotate(collider, self.game_object.Transform.rotation)
        object_transform = collider.get_rect(
			center = self.game_object.Transform.center)
        self.game_object.screen.blit(collider, object_transform)
        pass

    def set_collider_size(self, size):
        self.collider_size_orig = size
    
    def _get_final_cords(self, xy):
        rot = math.degrees(self.game_object.Transform.rotation)
        Rx = self.collider_transform[0] + (xy[0]  * math.cos(rot)) - (xy[1] * math.sin(rot))
        Ry = self.collider_transform[1] + (xy[0]  * math.sin(rot)) + (xy[1] * math.cos(rot))
        return [Rx, Ry]      


    
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

#https://www.jkh.me/files/tutorials/Separating%20Axis%20Theorem%20for%20Oriented%20Bounding%20Boxes.pdf#:~:text=In%202D%20space%2C%20the%20Separating%20Axis%20Theorem%20states,A%20and%20rectangle%20B%20in%20the%20illustration%20below.


'''
PA = coordinate position of the center of rectangle A
Ax = unit vector representing the local x-axis of A
Ay = unit vector representing the local y-axis of A
WA = half width of A (corresponds with the local x-axis of A)
HA = half height of A (corresponds with the local y-axis of A)
PB = coordinate position of the center of rectangle B
Bx = unit vector representing the local x-axis of B
By = unit vector representing the local y-axis of B
WB = half width of B (corresponds with the local x-axis of B)
HB = half height of B (corresponds with the local y-axis of B)


Let
T = PB – PA
L = an arbitrary axis (i.e. a unit vector)
Proj ( v ) = v • L = projection of v onto an axis, L
Then a separating axis, L, exists if and only if
|Proj ( T )| > ½|Proj ( RectangleA )| + ½|Proj ( RectangleB )|
which is equivalent to
|Proj ( T )| > |Proj ( WA*Ax )| + |Proj ( HA*Ay )| + |Proj ( WB*Bx )| + |Proj( HB*By )|
which is equivalent to
| T • L | > | ( WA*Ax ) • L | + | ( HA*Ay ) • L | + | ( WB*Bx ) • L | + |( HB*By ) • L |
where | s | denotes the absolute value of scalar s
'''