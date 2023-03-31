# Transform
Handles the movement of the game object and how that image will look when rendered on the screen. <br />
The main 3 attributes for each game object are transform, scale, and rotation. 

# Attributes

## User Set
| Attribute | discription|
| ---- | ---- |
| transform | where on the screen the image will render, by default (-1,-1) so it will appear off the screen | 
| scale | how much to scale the image. By default (1,1) so each pixel in the image will be one pixel on the screen. |
| rotation | how much to rotate the image from straight up and down in degrees. By default 0 |
|

## Auto filled/passed

| Attribute | discription|
| ---- | ---- |
| game_object | auto-passed-in. The instance of the game object that this class instance is a part of |
| last_scale | used to store the scale of the game object last physics frame. Look to __efficient_scaling__ for why this is | 
| last_parent_scale | same as last_scale but for the instance of the parent game object | 
| previous_scale | stores the scale that is returned from the _scale method and used to check for changes in the scale over time |
| size | the height and width in pixels of the raw image | 
| load | rotated and scaled image ready to be blit'ed onto the screen | 
| center | transformed coords for the image accounting for the parent's game object | 
| final_scale | the scaling amount actually used on the image to scale it |

# Efficient Scaling
To not have to recalculate the scale of the image every frame, a check is run to see if the scale has changed from what it was the last frame. If it or the scale of the parent has not changed, then the final_scale value will remain the same as the last frame.

# Methods

| Method | discription|
| ---- | ---- |
| start | Grabs the size value of the image. Done in start to make sure the image has been instantiated before trying to get the size | 
| update | Gets the transformed image accounting for rotation and scale | 
| add_transform | takes in x and y and adds them to the transform value to allow screen movement | 
| parent_transform | Transforms the coords to account for the transform of the parent game object. Calls the _rotate_transform method to do this. Fills the center attribute here. 
| _rotate_transform | takes in the rotation of the parent game object, and the (x,y) coords of the game object multiplied by the scale value of the parent to normalize for the scaling of the parent and gives the coords to rotate the child game object around the parent. | 
| _f_scale | Gets the scale value using the _scale method and transforms the raw image first by scaling it then by rotating it and returns that image. Uses the builtin pyGame methods transform.scale and rotate to do this|
| _scale | First checks if the scale or the parent scale has changed from last frame and if so returns the last final_scale amount. If not then runs _parent_scale and saves the value to previous_scale and updates _last_parent_scale to ready for next frame. | 
| _parent_scale | for the x and y scale values each, it multiplies the size (pixel amount) by the scale (for the child) by the scale (for the parent) and returns it |
