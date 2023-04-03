# Loading and Instantiating the game object

First we need to get our image for this tutorial we will use the python logo: <br />
![logo](logo.png)
<br />

Get this image or another online and download it as a png or jpg. <br />
Once done place the image in the data folder of src next to null.png. <br />

## Instantiating the game object.
Then in the variables.py file, add a line:
```python
GO("Logo", screen.screen, "logo.png", "origin", "transform.Transform", "bounce.Bounce")
```
This line starts by giving the game object the name: __Logo__. It then sets the object to render on the correct pyGame screen and sets the image to render as the name of the image you just put into the data folder. the __origin__ argument makes the parent origin so all the transforms are 1:1 to the screen. Finally, we add the __transform.Transform__ which allows you to move the object around the screen. <br />
Next we need to start the game object at the center of the screen. To do this we go into the game object and into the Transform package and from there to the transform variable. (this can be confusing but lower case transform is the coords on the screen and uppercase Transform is the entire package)
```python
GO.GAME_OBJECTS["Logo"].Transform.transform = [180, 240]
```
We enter the __GAME_OBJECTS__ dictionary in game_objects, GO, and call the key: Logo. We can access the attributes of that game object for example here we are calling the attribute Transform which is the instance of the Transform script for that game object. The points 180 and 240 are just half way across the screen to center the game object.<br />
We now have a game object that will be rendered to the center of the screen but will not move at all. <br />
Depending on the image, it may fill up too much of the screen and if so we can scale it down by, just like with the transform, accessing the attribute from the game object. 