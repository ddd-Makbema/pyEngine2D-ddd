# Variables
One of the main files that the user interacts with.<br />
This is where the user initializes the Screen and Game Objects<br />

## Initializing The Objects

In depth explanations of both methods can be found in [game objects](GameObject/GameObject.md) and [Screen](Screen.md)<br />

In short to make a new game object you need to just run the function, no need to save it as a variable.<br />
```python
#GameObject(name ,screen, sprite, parent, packages)
GameObject("test_object" ,screen.screen, "test.png", "origin", "transform.Transform")
```
For the screen, you do need to save it as a variable, "screen"<br />
```python
# screen = Init(width, height, fps, ffps, icon, name_window)
screen = Init(300, 280, 60, 100, "test.png", "myGame")
```

## Loading Scripts

To load a new script, make sure the script is in the "user" folder in "scripts" <br />
Then after the "parent" paramater, add as many scripts as you would like by listing the file its in then the class name.<br />
eg. "transform.Transform" or "Collider2D.RectangleCollider2D"

## Setting the Attributes
To set the attributes, you need to call the name you set the game object to when initializing it from a list. <br />
Then you can call the class using an attribute added to the game object class which is an instance of the script class.<br />
Using that you can access and modify all the attributes of the script.
```python
GO.GAME_OBJECTS["test_object"].Transform.rotation = 90
```