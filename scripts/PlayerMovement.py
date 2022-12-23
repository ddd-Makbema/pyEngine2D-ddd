from GameObject import *
from GameObject import GameObject
from dataTypes import Vector2D

class PlayerMovement:
	def __init__(self, gameObject):
		self.gameObject = gameObject
		GameObject.gameObjectDict["sam"] = gameObject
	def Update(self):
		#self.gameObject.transform = self.gameObject.transform + Vector2D(5,1)
		self.gameObject.rotation = self.gameObject.rotation + 1
		self.gameObject.scale = Vector2D(2.5,2.5)