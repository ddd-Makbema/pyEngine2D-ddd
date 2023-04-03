# Parent

Sets the frame of reference for the object to be rendered. <br />

by default the parent is pre-set as "origin" which has the scale set at 1, rotation to 0 and transform to 0,0 <br />
This makes it so whatever number is input for any of these values is 1:1 transformed to the screen. There are cases however, like making an arm on a body, which require multiple game objects to move across the screen without changing in relation to one another. this allows the user to do this by just moving or otherwise transforming the parent, and all the children will move by the same amount. For the most part, the parent is only by default used in the transform script, but it is possible to use the parent/child relation to transfer any information from the parent to the child. 
```python
#Here, the if statement checks if the parent's scale or the child's scale has changed and if so scales it using the _parent_scale method to scale the gameobject using both the game object and the parent's scale values.
# in self.game_object.parent_instance.Transform.scale, it follows, like a file path, the road to the value. 
#     it goes to the instance of the parent game object, helpfully stored in parent_instance, then goes to the instance of the Transform class inside that game object using the Transform attribute then grabs the scale from that. 
	if self.game_object.parent_instance.Transform.scale != self.last_parent_scale or self.scale != self.last_scale:
			self.previous_scale = self._parent_scale()
			self.last_parent_scale = self.game_object.parent_instance.Transform.previous_scale
```