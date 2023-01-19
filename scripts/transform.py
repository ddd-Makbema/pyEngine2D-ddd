from game_object import GameObject
from data_types import Vector2D
import pygame
import math


class Transform:
	def __init__(self, game_object):
		self.game_object = game_object
		self.transform = Vector2D(0,0) 
		self.scale = Vector2D(1,1)
		self.rotation = 0
		self.last_scale = Vector2D(-1,-1)
		self.last_parent_scale = Vector2D(-1,-1)
	
	def start(self):
		self.size = Vector2D(self.game_object.image_start.get_width(), self.game_object.image_start.get_height())
		
	def update(self):
		self.load = self._f_scale()
		
	def parent_transform(self):
		"""Returns the transform of the gameObject to local coords translated from the parent object. If there isn't a parent then returns normal coords."""

		rotate_trans = self._rotate_transform(self.game_object.parent_instance.Transform.rotation, 
			self.transform.x*self.game_object.parent_instance.Transform.scale.x, self.transform.y*self.game_object.parent_instance.Transform.scale.y)
		return rotate_trans
			
	def _scale(self):
		"""Scales the game object's pixels according to the scale number and the parent's scale number and returns it."""
		
		if self.game_object.parent_instance.Transform.scale != self.last_parent_scale or self.scale != self.last_scale:
			self.previous_scale = self._parent_scale()
			self.last_parent_scale = self.game_object.parent_instance.Transform.previous_scale
		return self.previous_scale

	def _parent_scale(self):
		"""scales the object according to the parent's scale value"""

		p_scale = (self.scale.x * self.size.x * self.game_object.parent_instance.Transform.scale.x,
					self.scale.y * self.size.y * self.game_object.parent_instance.Transform.scale.y)
		return p_scale

	def _rotate_transform(self, rotation, radius_x, radius_y):
		"""Transforms the child to account for the parent's rotation"""
		if self.game_object.parent != "origin":
			angle_rad = math.radians(180+rotation)
			x = radius_x * math.sin(angle_rad)
			y = radius_y * math.cos(angle_rad)
			return (x+self.game_object.parent_instance.Transform.transform.x,y+self.game_object.parent_instance.Transform.transform.y)
		else:
			return (self.transform.x,self.transform.y)
		

	def _f_scale(self):
		"""Scales the image accounting for parent/child transforms
  and returns the image to be rendered."""

		scale = self._scale()
		image = pygame.transform.scale(self.game_object.image_start , scale)

		image = pygame.transform.rotate(image, self.rotation+self.game_object.parent_instance.Transform.rotation)
		return image

if __name__ == '__main__':
    pass