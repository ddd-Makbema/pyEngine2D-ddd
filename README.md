# gameEngine

A game engine built using pygame based off of the Unity game engine.

## Installation

1: Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```
2: Go to variables.py and make a [screen object](ScreenInit.md)
	go below to see examples of how to do this
	Save the screen as "screen"

3: Initialize all the [game objects](game%20objects.md) you want underneath the screen in variables.py
	To set attributes for user-made scripts call the game object from the dictionary then follow the path to the attribute

4: Load all media(images, sound, etc) into the "data" folder  

5: Write the main game code into ".py" files in the "scripts/user" folder
	there are two folders in scripts; "user" and "builtins" you only need to look at user
  	a sample file is provided in the script/user folder already
 	make sure to load all the packages you want by naming the file and class name at the end of the game object declaration
  
6: Finally run the "main.py" file to run the game
## Code Samples

### variables.py
```python
from game_object import GameObject as GO
from screen_init import ScreenInit

# Creates a screen to run the game on
# screen = Init(width, height, fps, ffps, icon, name_window)
screen = Init(300, 280, 60, 100, "test.png", "myGame")

# initializes a game object onto the game screen
#loads in the script "Transform" to allow the go to be rendered on the screen and moved
#"origin" is the default parent
GameObject(name ,screen, sprite, parent, packages)
GameObject("test_object" ,screen.screen, "test.png", "origin", "Transform.transform")

#setting the attributes
GO.GAME_OBJECTS["test_object"].Transform.transform = [0,0]
GO.GAME_OBJECTS["test_object"].Transform.rotation = 0
```

### player_movement.py
```python
from game_object import GameObject

class PlayerMovement:
	def __init__(self, game_object):
		self.game_object = game_object
	def fixed_update(self):
		'''Every physics frame rotate the image by 1 degree and multiply the scale by 0.999'''
		self.game_object.Transform.rotation = self.game_object.Transform.rotation - 1
		self.game_object.Transform.scale = [self.game_object.Transform.scale[0] * 0.999, self.game_object.Transform.scale[1] * 0.999]
		
	#notice there is no update you do not need all the methods overriden in the player made scripts for it to run properly
if __name__ == '__main__':
    pass
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
