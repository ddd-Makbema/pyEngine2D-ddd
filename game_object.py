
import pygame
from data_types import Vector2D
from exceptions import SpriteNameError
import os
import math

class GameObject():
	"""Allows calling of user made packages amd inter-file communication 
 of instance variables.

	Auto imports files from data specified by when creating each instance 
	of game object. It allows communication between different game 
	objects in all files as well as overridable functions such as Update
	for each user made package.

	Attributes:
 		INSTANCES: list of all instances of game objects
   		NAMES: list of each user defined name for the game objects
	 	GAME_OBJECTS: dictionary keying the name of game objects to the instance
   		sprite: a string containing the name of the image from the data file
	 	screen: default value contains the instance of the pygame screen defined in main
   		transform: contains the Vector2D(x,y) screen coords for the image to be loaded
	 	scale: contains the Vector2D(x,y) scale amount with 1 being default pixel size
	 	rotation: contains a int of the degrees to rotate the image from up and down
   		parent: string with the name of the game object to inherit Transform from.
   		packages: a list of strings for file names you want to import
		last_scale: int of scale from last frame to reduce operations per frame
		last_parent_scale: int same as last_scale but for the parent object if there is one
		image_start: screen image of the sprite entered with 0 rotation and 1 scale modified each frame.
		package_instances: list of instances of classes loaded from packages entered in args
		packages_import: temporary list of imported packages from scripts folder to be instantiated
"""
	INSTANCES = []
	NAMES = []
	GAME_OBJECTS = {}

	def __init__(self, name ,screen, sprite="null.png",  transform=Vector2D(0,0), scale=Vector2D(1,1), rotation=0, parent=None, *args):
		"""Initializes game object and adds the instance to all the lists"""
		self.sprite = "data/" + sprite #data/ is to pull the image files from the data folder
		self.screen = screen 
		self.transform = transform 
		self.scale = scale
		self.rotation = rotation
		self.packages = args
		self.parent = parent
		self.name = name
		self.last_scale = None
		self.last_parent_scale = None
		self.image_start = None

		self.package_instances = [] 
		self.packages_import = []
		GameObject.NAMES.append(name) 
		GameObject.INSTANCES.append(self) 
		GameObject.GAME_OBJECTS[self.name] = self

		#makes sure there can not be two conflicting names.
		if name in GameObject.NAMES:
			i = 1
			while name in GameObject.NAMES:
				name = name + f"({i})"
				i += 1
		
		

	def start(self):
		"""Initializes the sprite as an object and imports all packages needed. And calls the start funtions for them."""

		self.image_start = _pyLoad(self.sprite)
		self.size = Vector2D(self.image_start.get_width(), self.image_start.get_height())

		#initializes the parent instance if one was entered
		if self.parent:
			self.parent_instance = GameObject.GAME_OBJECTS[self.parent]
		else:
			self.parent_instance = None

		#initializes the packages for the game object
		for script in self.packages:
			full_module_name = "scripts." + script
			self.packages_import.append(self._import_class_from_string(full_module_name))
		for pack in self.packages_import:
			self.package_instances.append(pack(self))

		#calls the start function for all packages if they have them
		for p in self.package_instances:
			try:
				p.Start()
			except AttributeError:
				pass
		return


	def update(self):
		"""Called for each game object each frame from main. Calls the update 
  			function for all packages imported. Scales and Rotates 
	 the game object as needed."""
	
		self.load = self._f_scale()

		#calls the update function for all packages if they have them
		for p in self.package_instances:
			try:
				p.update()
			except AttributeError:
				pass
		return
		
	def fixed_update(self):
		"""Same as update but for fixed update: physics calculations"""

		#calls the fixed update function for all packages if they have them
		for p in self.package_instances:
			try:
				p.fixed_update()
			except AttributeError:
				pass
		return

	def parent_transform(self):
		"""Returns the transform of the gameObject to local coords translated from the parent object. If there isn't a parent then returns normal coords."""
	
		if not self.parent:
			return (self.transform.x,self.transform.y)
		else:		
			rotate_trans = self._rotate_transform(self.parent_instance.rotation, 
				self.transform.x*self.parent_instance.scale.x, self.transform.y*self.parent_instance.scale.y)
			return rotate_trans
			
	def _scale(self):
		"""Scales the game object's pixels according to the scale number and the parent's scale number and returns it."""
		
		if not self.parent:
			if self.scale != self.last_scale:
				self.last_scale = self.scale
				scale = (self.scale.x * self.size.x, self.scale.y * self.size.y)
				self.previous_scale = scale
				return scale
			return self.previous_scale
		elif self.parent_instance.scale != self.last_parent_scale or self.scale != self.last_scale:
			p_scale = self._parent_scale()
			return p_scale
		return self.previous_scale

	def _parent_scale(self):
		"""scales the object according to the parent's scale value"""

		self.last_scale = self.scale
		self.last_parent_scale = self.parent_instance.scale
		p_scale = (self.scale.x * self.size.x * self.parent_instance.scale.x,
					self.scale.y * self.size.y * self.parent_instance.scale.y)
		self.previous_scale = p_scale
		return p_scale

	def _rotate_transform(self, rotation, radius_x, radius_y):
		"""Transforms the child to account for the parent's rotation"""

		angle_rad = math.radians(180-rotation)
		x = radius_x * math.sin(angle_rad)
		y = radius_y * math.cos(angle_rad)
		return (x+self.parent_instance.transform.x,y+self.parent_instance.transform.y)

	def _f_scale(self):
		"""Scales the image accounting for parent/child transforms
  and returns the image to be rendered."""

		scale = self._scale()
		image = pygame.transform.scale(self.image_start , scale)

		if self.parent:
			image = pygame.transform.rotate(image, self.rotation-self.parent_instance.rotation)
		else:
			image = pygame.transform.rotate(image, -self.rotation)
		return image
	
	def _import_class_from_string(self, string_name):
		"""Given a string like 'module.submodule.func_name' which refers to a 	function, return that function so it can be called
 		Returns:
  			instance of the package imported from the string"""

		mod_name, func_name = string_name.rsplit(".", 1)
		mod = __import__(mod_name)

		for i in mod_name.split(".")[1:]:
			mod = getattr(mod, i)
		return getattr(mod, func_name)

def _pyLoad(sprite_to_load):
	"""Shorter function to load and return a pygame image type variable while 
 		also calling a more descriptive exception if the sprite doesn't exist."""
		
	if not (os.path.exists(sprite_to_load)):
		raise SpriteNameError(sprite_to_load.strip("data/"))
	return pygame.image.load(sprite_to_load).convert_alpha()