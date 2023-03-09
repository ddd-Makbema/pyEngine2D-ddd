# Game Object
Main class to hold all the event handlers of the engine including user made packages.
### More in depth
This is where the hub of most of your game will run. This has built in functions that are called from main or packages such as colliders. When these functions are called, they will rarely do anything on their own, but instead try to call the function for all the packages listed in that game object. For each package, it will see if it has that package and if so, run the function in that package. 
It also currently takes care of handling the sprite using the information given from transform and giving the rendering information to the [main loop](../GameLoop.md). Eventually this feature will be moved to its own package in [builtins](Builtins), but that has not happened yet.

## Attributes
### Class Attributes

| Attribute | discription|
| ---- | ---- | 
| [INSTANCES](Attributes/ClassAttributes/INSTANCES.md) | A list of all the instances of game objects|
| [NAMES](Attributes/ClassAttributes/NAMES.md) | A list of the user-input names of the game objects|
| [GAME_OBJECTS](Attributes/ClassAttributes/GAME_OBJECTS.md) | A dictionary allowing the user to lookup any instance using any name|
### Instance Attributes
| Attribute | discription|
| ---- | ---- |
| name | The name this game object will be referenced by |
| screen | The instance of the screen loaded from the [screen](../Screen.md) |
| [sprite](Attributes/InstanceAttributes/sprite.md) | The name of the sprite to load from the data folder|
| [parent](Attributes/InstanceAttributes/parent.md) | Transforms the game object to this game object's local scale |
| [packages](Attributes/InstanceAttributes/packages.md) | All the user made or builtin packages in the scripts folder to put in for this game object |
#### Auto-set
| Attribute | discription|
| ---- | ---- |
| image_start | The original image loaded from data with no transforms on it|
| [package_instances](Attributes/InstanceAttributes/packages.md) | list of all the instances of packages to turn them into attributes|
| [parent_instance](Attributes/InstanceAttributes/parent.md) | the instance of the parent game object to access its transform and other key values|

## Methods
| Method | discription|
| ---- | ---- |
