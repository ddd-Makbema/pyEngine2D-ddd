from game_object import GameObject
from data_types import Vector2D

class PlayerMovement:
	def __init__(self, game_object):
		self.game_object = game_object
	def fixed_update(self):
		# self.game_object.transform += Vector2D(2.5,0.5)
		self.game_object.rotation = self.game_object.rotation + 1
		# self.game_object.scale = self.game_object.scale * 0.99