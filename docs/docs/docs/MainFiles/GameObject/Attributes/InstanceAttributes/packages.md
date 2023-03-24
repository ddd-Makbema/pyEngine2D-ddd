# Packages and Scripts

These will be how the main code that the user writes will be called. <br />

in the init function, it will import the scripts requested by the user, when instantiating the game object. It will then make two versions of the string, one that has the builtins folder in scripts as the destination adn one with the user folder. then it calls _import_class_from_string to get an instance of that class. it then will add that instance to the __package_instances__ attribute, which are used for every method call. When calling a method, for example the update method, it will iterate through everything in __package_instances__ and try to call the update method in the script. the script does not need to have an update method and if it doesn't, then nothing happens and it will carry on without errors. 
```python
for p in self.package_instances:
	try:
		p.update()
	except AttributeError as e:
		if "object has no attribute 'update'" in str(e):
			pass

		else:
			raise e
```

## Making a new script
Inside the scripts folder, there is a folder called "user." make a new python file called whatever you want and make a new class in it. It is possible to have multiple classes in the same file like with collisions, where all the collider and collision handler classes are in one file but can be independently put on to different game objects. <br />

Inside the new class, the init method requires two arguments, self and game_object. Self is self-explanatory. game_object is parsed in when the class is instantiated by each instance of game object. This is to allow you to check and change attributes in the game object itself as well as in other scripts attached to the game object. 
```python
#calling the image_start attribute from the game object instance that has this instance of Transform. 
self.game_object.image_start
```
To recive events, there are builtin and user made (not added yet) events that are called by the game object for every attached script. One example is the update function which is called once a frame. When it is called, the main game loop calls the update function for every game object, which then calls the update function for each attached script. More indepth descriptions of the possible events are elsewhere in the documentation. <br />
When adding these functions only pass in self as an argument and make sure the method name is spelled correctly. 
```python
def update(self):
	self.load = self._f_scale()
```
## Adding the script to different game objects. 
When first instantiating any game object, there are an indeterminate amount of packages that can be added. After the "parent" argument, the rest of the instantiation can be used for the packages. When naming the script it is only required to call the name of the file and the name of the class, not the full file path.<br />
```python
GO("katz", screen.screen, "null.png", "origin", "transform.Transform", "Collider2D.RectangleCollider2D", "player_movement.PlayerMovement")
``` 
Once it is instantiated, the script's instance is set as an attribute for the game object with the name being the name of the class.<br />
As stated above, this will only pass in self and game_object. To pass in additional arguments, you need to call the instance of the class and individually set each attribute. This is also where the __GAME_OBJECTS__ class attribute comes in, because to call each game object, you just call the name input earlier as the key for the dictionary. 
```python 
GO.GAME_OBJECTS["katz"].Transform.rotation = 0
```