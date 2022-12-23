from game_object import GameObject
from data_types import Vector2D

class PlayerMovement:
	def __init__(self, gameObject):
		self.gameObject = gameObject
		GameObject.gameObjectDict["sam"] = gameObject
	def Update(self):
		#self.gameObject.transform = self.gameObject.transform + Vector2D(5,1)
		self.gameObject.rotation = self.gameObject.rotation + 1