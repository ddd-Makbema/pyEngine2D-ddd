from GameObject import *
from GameObject import GameObject
from dataTypes import *

class PlayerMovement:
	def __init__(self, gameObject):
		self.gameObject = gameObject
		GameObject.gameObjectDict["sam"] = gameObject
	def Update(self):
		self.gameObject.transform = self.gameObject.transform + Vector2D(1,1)
		self.gameObject.scale = Vector2D(10,10)
		