
import pygame
import importlib
import ast
from pyEngine2D_ddd.exceptions import SpriteNameError
from pyEngine2D_ddd.exceptions import MultInstanceError
import os

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
   		parent: string with the name of the game object to inherit Transform from.
   		packages: a list of strings for file names you want to import
		image_start: screen image of the sprite entered with 0 rotation and 1 scale modified each frame.
		package_instances: list of instances of classes loaded from packages entered in args
		packages_import: temporary list of imported packages from scripts folder to be instantiated
"""
	INSTANCES = []
	NAMES = []
	LAYERS = []
	GAME_OBJECTS = {}
	LAYERS_INSTANCES = {}

	def __init__(self, name ,screen, sprite="null.png", parent="origin", tag="", layer="", *args):

		"""Initializes game object and adds the instance to all the lists"""
		self.sprite = sprite 
		self.screen = screen 
		self.packages = args
		self.parent = parent
		self.name = name
		self.image_start = None
		self.tag = tag
		self.layer = layer
		self.package_instances = []
		self.package_names = []
		#makes sure there can not be two conflicting names.
		added_name = self.name
		if self.name in GameObject.NAMES:
			i = 1 
			while added_name in GameObject.NAMES:
				added_name = self.name + f"({i})"
				i += 1
			self.name = added_name
		GameObject.NAMES.append(self.name) 
		GameObject.INSTANCES.append(self) 
		GameObject.GAME_OBJECTS[self.name] = self
		if self.layer not in GameObject.LAYERS:
			GameObject.LAYERS.append(self.layer)
			GameObject.LAYERS_INSTANCES[self.layer] = [self]
		else:
			GameObject.LAYERS_INSTANCES[self.layer].append(self)

		#initializes the packages for the game object
		for script in self.packages:
			full_module_name = "pyEngine2D_ddd.scripts." + script
			user_module_name = script
			tempInst = self._import_class_from_string(user_module_name, full_module_name)(self)
			name = script.rsplit(".", 1)[1]	
			
			#maybe later make this more efficient
			if tempInst.MULTIPLE_INSTANCES:
				init_name = name
				c = 0
				while name in self.package_names:
					name = init_name + "_" + str(c)
					c += 1

			elif name in self.package_names:
				raise MultInstanceError(name)

			self.package_instances.append(tempInst)
			self.package_names.append(name)
			setattr(self, name, tempInst)
		self.start()

	def delete(self):
		GameObject.GAME_OBJECTS.pop(self.name)
		GameObject.INSTANCES.remove(self)
		GameObject.NAMES.remove(self.name)
		return


	def new_game_object():
		"""updates the class level vars to account for the new game objects"""
		if GameObject.LAYERS != GameObject.load_previous_layers():
			GameObject.rendering_order_sort()
			# GameObject.collision_matrix_sorter()
# 
# 
# 
# 
# 
# 
			print("new list")

	def old_game_object():
		"""Loads the previous rendering order from file"""
		with open("pyEngine2D_ddd/data/rendering_order.txt", "r") as save:
			init_list = (save.read().splitlines())[0]
			ret = ast.literal_eval(init_list)
		GameObject.LAYERS = list(ret)			
		GameObject.INSTANCES = []
		for layer in GameObject.LAYERS:
			for game_object in layer:
				GameObject.INSTANCES.append(game_object)

	def load_previous_layers():
		with open("pyEngine2D_ddd/data/rendering_order.txt", "r") as save:
			init_list = (save.read().splitlines())[0]
			ret = ast.literal_eval(init_list)
		return ret



	def start(self):
		"""Initializes the sprite as an object and imports all packages needed. And calls the start funtions for them."""

		self.image_start = _pyLoad(self.sprite)
		#initializes the parent instance if one was entered
		try:
			self.parent_instance = GameObject.GAME_OBJECTS[self.parent]
		except KeyError as e:
			if self.parent in str(e):
				self.parent_instance = None
			else:
				raise e

		#calls the start function for all packages if they have them
		for p in self.package_instances:
			try:
				p.start()
			except AttributeError as e:
				if "object has no attribute 'start'" in str(e):
					pass

				else:
					raise e					

		return


	def update(self):
		"""Called for each game object each frame from main. Calls the update 
  			function for all packages imported. Scales and Rotates 
	 the game object as needed."""

		#calls the update function for all packages if they have them
		for p in self.package_instances:
			try:
				p.update()
			except AttributeError as e:
				if "object has no attribute 'update'" in str(e):
					pass

				else:
					raise e
		return
		
	def fixed_update(self):
		"""Same as update but for fixed update: physics calculations"""

		#calls the fixed update function for all packages if they have them
		for p in self.package_instances:
			try:
				p.fixed_update()
			except AttributeError as e:
				if "object has no attribute 'fixed_update'" in str(e):
					pass

				else:
					raise e

		return

	def on_collision_enter(self):
		for p in self.package_instances:
			try:
				p.on_collision_enter()
			except AttributeError as e:
				if "object has no attribute 'on_collision_enter'" in str(e):
					pass

				else:
					raise e

		return

	def on_trigger_enter(self):
		for p in self.package_instances:
			try:
				p.on_trigger_enter()
			except AttributeError as e:
				if "object has no attribute 'on_trigger_enter'" in str(e):
					pass

				else:
					raise e

		return
	
	def rendering_order_sort():
		"""changes the INSTANCES list to the order, first to last. Follow the instructions in command line. 
		That order is saved and can then be called the next time. To run, call this function from the main 
		file after instantiating the game objects to be rendered"""
		index = ""
		print("""You have entered the rendering order sorter. Follow the instructions in the console to set the 
		order. collision handler, origin and game objects like those that you don't recognize making are builting game objects to
		handle default values or act as different event handlers. They can be moved but it is reccomended not to."""
		)
		while index != "n":
			print("Right now rendering order is: " + str(GameObject.LAYERS))
			index = input("Which index would you like to change? (starting from 0 on the left) (input n to break) ")
			if index == "n":
				GameObject._save_order()
				print("The game is now running again with the updated order and the new order is saved to the data folder.")
				return
			else:
				try:
					temp_obj = GameObject.LAYERS.pop(int(index))
				except:
					print("That input is not valid. It may not be an int or out of range")
					continue
			final_loc = input("Which index would you like the object to be moved to? ")
			try:
				GameObject.LAYERS.insert(int(final_loc), temp_obj)
			except:
				print("That input is not valid for destination. It may not be an int or out of range")
				continue
			print("it has been done") # just realized how ominous this sounds
		return

	def _save_order():
		with open("pyEngine2D_ddd/data/rendering_order.txt", "w") as save:
			save.write(str(GameObject.LAYERS))

	def collision_matrix_sorter():
		"""Used to edit the collision layer matrix."""
		try:
			collision_matrix = load_collision_matrix()
		except MissingCollisionMatrixError as e:
			collision_matrix = init_collision_matrix()
		print("The collision matrix is:")
		self.print_collision_matrix()
		modify = input("What collider pair do you want to modify? [across, down] (index not name)")
		print(list(modify))

	def print_collision_matrix(collision_matrix):
		print(GameObject.LAYERS)
		for i in range(len(collision_matrix)):
			print(GameObject.LAYERS[-i-1], end=' ')
			print(collision_matrix[i])		

	def load_collision_matrix():
		pass

	def init_collision_matrix():
		pass

	def _import_class_from_string(self, string_name, name_secondary):
		"""Given a string like 'module.submodule.func_name' which refers to a 	function, return that function so it can be called
 		Returns:
  			instance of the package imported from the string"""
		try:
			mod_name, func_name = string_name.rsplit(".", 1)
			mod = __import__(mod_name)
			importlib.reload(mod)
			for i in mod_name.split(".")[1:]:
				mod = getattr(mod, i)
			return getattr(mod, func_name)
		except ModuleNotFoundError as e:
			mod_name, func_name = name_secondary.rsplit(".", 1)
			mod = __import__(mod_name)
			for i in mod_name.split(".")[1:]:
				mod = getattr(mod, i)
			return getattr(mod, func_name)
def _pyLoad(sprite_to_load):
	"""Shorter function to load and return a pygame image type variable while 
 		also calling a more descriptive exception if the sprite doesn't exist."""
		 
	if not (os.path.exists(sprite_to_load)):
		raise SpriteNameError(sprite_to_load.strip("pyEngine2D/data/"))
	return pygame.image.load(sprite_to_load).convert_alpha()

if __name__ == '__main__':
	pass