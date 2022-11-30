from GameObject import *
from GameObject import GameObject
from dataTypes import *

class PlayerMovement:
	def __init__(self, gameObject):
		self.gameObject = gameObject
		GameObject.gameObjectDict["sam"] = gameObject
	def Update(self):
		self.gameObject.transform = Vector2D(100,100)
		self.gameObject.rotation = self.gameObject.rotation + 1
