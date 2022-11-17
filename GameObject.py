import pygame
from dataTypes import Vector2D
import importlib


class GameObject():
	#Global variables to get different aspects of GO
	#list of the instances of each gameObject
	instanceList = []
	#list of the names of each gameObject
	listNames = []
	#each name mapped to an instance of the gameObject
	gameObjectDict = {}
	def __init__(self, name ,screen, sprite="null.png",  transform=Vector2D(0,0), rotation=0, Fps=60, Ffps=100, *args):
		self.sprite = "data/" + sprite #what image to load
		self.screen = screen #default variable for the pygame screen
		self.transform = transform #XY coords of the image
		self.rotation = rotation #rotation of the image
		self.packages = args #name of the user made packages to load from scripts
		'''names each gameObject and makes sure that there are no duplicates '''
		if name in GameObject.listNames:
			i=1
			while name in GameObject.listNames:
				name = name + f"({i})"
				i+=1
		self.name = name #name for player to id the go's
		GameObject.listNames.append(name) #adds it to a list of all game object names
		GameObject.instanceList.append(self) #adds the instance of the game object to a list
		self.packageList = [] #all user made scripts to load later
		self.packageInstance = [] #list of instances of user made scripts
		GameObject.gameObjectDict[self.name] = self #adds this game object to a dictionary of all game objects
		
		

	def start(self):
		self.load = pygame.image.load(self.sprite)
		for script in self.packages:
			full_module_name = "scripts." + script + "." + script
			self.packageList.append(import_class_from_string(full_module_name))
		

		for pack in self.packageList:
			self.packageInstance.append(pack(self))

			
		return pygame.image.load(self.sprite)


	def Update(self):
		for p in self.packageInstance:
			try:
				p.Update()
			except AttributeError:
				pass
				
		return
	def FixedUpdate(self):
		for p in self.packageInstance:
			try:
				p.FixedUpdate()
			except AttributeError:
				pass
				
		return

def import_class_from_string(string_name):
    """Given a string like 'module.submodule.func_name' which refers to a function, return that function so it can be called"""
    # Split the string_name into 2, the module that it's in, and func_name, the function itself
    mod_name, func_name = string_name.rsplit(".", 1)

    mod = __import__(mod_name)
    # ``__import__`` only gives us the top level module, i.e. ``module``, so 'walk down the tree' getattr'ing each submodule.
    # from http://docs.python.org/faq/programming.html?highlight=importlib#import-x-y-z-returns-module-x-how-do-i-get-z
    for i in mod_name.split(".")[1:]:
        mod = getattr(mod, i)

    # Now that we have a reference to ``module.submodule``, ``func_name`` is available as an attribute to that, so return it.
    return getattr(mod, func_name)
