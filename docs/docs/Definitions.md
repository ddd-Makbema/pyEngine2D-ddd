# Definitions 

## Game Engine Terminology

### GameObject
The main objects manipulated during runtime <br />
Used for: <br />
    - Event handling<br />
    - Rendering images on the screen<br />
    - Calling other scripts<br />
### Screen
Where the game is rendered<br />
### Transform
Attributes
### Parent
Set as the origin for where the image is rendered<br />
multiplies the scale by the parent's scale<br />
adds the rotation to the parent's rotation<br />
adds the coords of the image to the parent's<br />
when the parent is rotated the child is rotated around it
### Sprite
The image loaded and transformed that is put on the screen
### Frame/FPS
The Screen refreshing to update with physics and other changes<br />
Fps is how fast the updates happen
### Fixed FPS
Will be ran a set amount of times a second. <br />
Good for physics and computations where you<br />
do not want everything to go super speedy if <br />
someone is using a faster computer  