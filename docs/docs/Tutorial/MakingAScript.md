# Making a script
We now have a game object that can render onto the screen, but it does not move. Our script will now add that. <br />

To make the script we need to go into src/scripts/user. In here let's make a script: bounce.py. <br />

Inside the file let's start by importing two packages. These are not nessesary to this script we are writing but are for bigger files so it is good to add them. 
```python
from src.game_object import GameObject
import pygame
```
We first need an the init function with two arguments: self and game_object. Any attributes that need to be added we can do that seperatly after instantiating the game object.<br />
```python
def __init__(self, game_object):
	self.game_object = game_object
```
Now because we are just rendering this and do not care about percise movements, we are going to put the code into the update method. <br />

Before that however, we will make two instance attributes: x_speed and y_speed. These can be changed in the variables file like how we changed the transform value. <br />
```python
# y is set to negative because we want to start with it going to the top right corner and (0,0) is in the top left.
def start(self):
    self.x_speed = 5
    self.y_speed = -5
```
Now for update we will need code to move the image and some more to check if the image is bouncing out of the screen.<br />
The movement is quite easy, we just need to call the __add_transform__ method in Transform. <br />
```python
# it takes in the x and y value to move it by so we can just add the speed values.
self.game_object.Transform.add_transform(self.x_speed, self.y_speed)
```
Next to check if the image goes off the screen. To do this, we need to check if the image's x or y is less than 0 because then the image would be off the screen to the left/top. Then to check for the right/bottom, we will grab the width value for screen from the screen class. <br />