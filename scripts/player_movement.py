from game_object import GameObject
from data_types import Vector2D

class PlayerMovement:
	def __init__(self, game_object):
		self.game_object = game_object
		GameObject.GAME_OBJECTS["sam"] = game_object
	def update(self):
		self.game_object.transform = self.game_object.transform + Vector2D(5,1)
		self.game_object.rotation = self.game_object.rotation + 1
		self.game_object.scale = self.game_object.scale * 0.99