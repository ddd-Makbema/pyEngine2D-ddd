# Game Object
Main class to hold all the event handlers of the engine including user made packages.
### More in depth
This is where the hub of most of your game will run. This has built in functions that are called from main or packages such as colliders. When these functions are called, they will rarely do anything on their own, but instead try to call the function for all the packages listed in that game object. For each package, it will see if it has that package and if so, run the function in that package. 
It also currently takes care of handling the sprite using the information given from transform and giving the rendering information to the [main loop](../GameLoop.md). Eventually this feature will be moved to its own package in [builtins](Builtins), but that has not happened yet.

## Attributes
### Class Attributes

| Attribute | discription|
| ---- | ---- | 
| [INSTANCES](Attributes/classAttributes.md) | A list of all the instances of game objects|
| [NAMES](Attributes/classAttributes.md) | A list of the user-input names of the game objects|
| [GAME_OBJECTS](Attributes/classAttributes.md) | A dictionary allowing the user to lookup any instance using any name|

### Instance Attributes

| Attribute | discription|
| ---- | ---- |
| name | The name this game object will be referenced by |
| screen | The instance of the screen loaded from the [screen](../Screen.md) |
| sprite | The file path of the [sprite](../../../Definitions) to load from the data folder|
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
| __init__ | sets most class attributes and imports [scripts](../../Builtins)|
| [start](Methods/start.md) | Initializes the [sprite](../../../Definitions) and loads the instance of the parent also calls the start method in all scripts|
| [update](Methods/update.md) | called each frame from the [MainGameLoop](../GameLoop.md) will call update method in all scripts | 
| [fixed_update](Methods/update.md) | called each [physicsFrame](../../../Definitions), will have eventual consistency so it is good for physics, calls fixed_update method in all scripts |
| [on_collision_enter](Methods/collisionMethods.md) | called by the collision handler, calls on_collision_enter for the scripts |
| [on_trigger_enter](Methods/collisionMethods.md) | same as collision enter but for trigger boxes | 
| _import_class_from_string | takes in two strings containing the file path for the script, either from builtins or user folders, returns the instance of the script specified by the input string. will search the user folder first then the builtins.| 
| _pyLoad | takes in the file path of the image stored in the data folder and returns the image loaded using  pyGame and the convert_alpha() method to make it transparent so it doesnt show up as a rectangle |

## Instantiating the class
###### To instantiate the class, the arguments are passed in as follows:
| Attribute | Result |
| ---- | ---- |
| name | string of the name that the game object will be called in the dictionary of all game objects |
| screen | should be the same for all game objects, screen.screen, from when the screen was instantiated. This is where the game object will be rendered |
| sprite | file name of the image that you want displayed for the game object. No need to put the full filepath, just make sure to put the image in the data folder. |
| parent | By default, this is set to origin, which causes all inputs to directly transform to screen cords. this is the name of the game object you wish to have as the parent if you want one. |
| args | all the scripts you want to add to the game object |