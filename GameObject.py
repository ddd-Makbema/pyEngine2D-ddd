
import pygame
from dataTypes import Vector2D
from Exceptions import SpriteNameError
import os

class GameObject():
	"""Allows calling of user made packages amd inter-file communication 
 of instance variables.

	Auto imports files from data specified by when creating each instance 
	of game object. It allows communication between different game 
	objects in all files as well as overridable functions such as Update
	for each user made package.

	Attributes:
 		instanceList: list of all instances of game objects
   		listNames: list of each user defined name for the game objects
	 	gameObjectDict: dictionary keying the name of game objects to the instance
   		sprite: a string containing the name of the image from the data file
	 	screen: default value contains the instance of the pygame screen defined in main
   		transform: contains the Vector2D(x,y) screen coords for the image to be loaded
	 	scale: contains the Vector2D(x,y) scale amount with 1 being default pixel size
	 	rotation: contains a int of the degrees to rotate the image from up and down
   		parent: string with the name of the game object to inherit Transform from.
   		packages: a list of strings for file names you want to import

"""
	instanceList = []
	listNames = []
	gameObjectDict = {}
	def __init__(self, name ,screen, sprite="null.png",  transform=Vector2D(0,0), scale=Vector2D(1,1), rotation=0, parent=None, *args):
		"""Initializes game object and adds the instance to all the lists"""
		self.sprite = "data/" + sprite 
		self.screen = screen 
		self.transform = transform 
		self.scale = scale
		self.rotation = rotation
		self.packages = args
		self.parent = parent
		if name in GameObject.listNames:
			i=1
			while name in GameObject.listNames:
				name = name + f"({i})"
				i+=1
		self.name = name
		GameObject.listNames.append(name) 
		GameObject.instanceList.append(self) 
		self.packageList = [] 
		self.packageInstance = [] 
		GameObject.gameObjectDict[self.name] = self 
		
		

	def start(self):
		"""Initializes the sprite as an object and imports all packages needed. And calls the start funtions for them.\n
  		Returns: \n
			a pygame image object with the sprite from data loaded as the sprite and saves the size of the image"""
		self.loadStart = pyLoad(self.sprite)
		self.currentRotation = 0
		self.size = Vector2D(self.loadStart.get_width(), self.loadStart.get_height())
		for script in self.packages:
			full_module_name = "scripts." + script + "." + script
			self.packageList.append(self.import_class_from_string(full_module_name))
			

		for pack in self.packageList:
			self.packageInstance.append(pack(self))
		for p in self.packageInstance:
			try:
				p.Start()
			except AttributeError:
				pass
			
		return


	def Update(self):
		"""Called for each game object each frame from main. Calls the update 
  			function for all packages imported. Scales and Rotates 
	 the game object as needed."""
	
		for p in self.packageInstance:
			
			try:
				p.Update()
			except AttributeError:
				pass
		self.load = self.rotateAndScale()
		return
		
	def FixedUpdate(self):
		"""Same as update but for fixed update: physics calculations"""
		for p in self.packageInstance:
			try:
				p.FixedUpdate()
			except AttributeError:
				pass
				
		return

	def ParentTransform(self):
		"""Returns the transform of the gameObject to local coords translated from the parent object. If there isn't a parent then returns normal coords."""
		if not self.parent:
			return (self.transform.x,self.transform.y)
		else:
			parent = GameObject.gameObjectDict[self.parent]
			localPosition = ((self.transform.x + parent.transform.x * parent.scale.x),
					(self.transform.y + parent.transform.y * parent.scale.y))
			
			return localPosition
	def ParentScale(self):
		if not self.parent:
			return (self.scale.x * self.size.x, self.scale.y * self.size.y)
		
		pScale = (self.scale.x * self.size.x * 
				  GameObject.gameObjectDict[self.parent].scale.x
				  , self.scale.y * self.size.y * 
				  GameObject.gameObjectDict[self.parent].scale.y)
		return pScale

	def rotateAndScale(self):
		"""Rotates and Scales the image accounting for parent/child transforms\n
  and returns the image to be rendered."""
		scale = self.ParentScale()
		image = pygame.transform.scale(self.loadStart, scale)
		image = pygame.transform.rotate(image, self.rotation)
		return image
	
	def import_class_from_string(self, string_name):
		"""Given a string like 'module.submodule.func_name' which refers to a 	function, return that function so it can be called
 		Returns:
  			instance of the package imported from the string"""
		mod_name, func_name = string_name.rsplit(".", 1)
	
		mod = __import__(mod_name)
		for i in mod_name.split(".")[1:]:
			mod = getattr(mod, i)
		
		return getattr(mod, func_name)

def pyLoad(sprite_to_load):
	"""Shorter function to load and return a pygame image type variable while 
 		also calling a more descriptive exception if the sprite doesn't exist."""
	if not (os.path.exists(sprite_to_load)):
		raise SpriteNameError(sprite_to_load.strip("data/"))
	return pygame.image.load(sprite_to_load)