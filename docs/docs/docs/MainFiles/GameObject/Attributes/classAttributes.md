# GAME_OBJECTS INSTANCES and NAMES

instance and names are lists <br />
game_objects is a dictionary <br />

during init, Names will be appended with just the name put in by the user when defining the game object.
Instances will just have self appended to the list.  <br />
Neither of these are particuarly useful but they are used to append this information to GAME_OBJECTS. <br />
GAME_OBJECTS is a dictionary which contains the instances of the classes keyed to the names given by the user to be called like a variable but also allows up to iterate through every game object instance. This is useful for calling functions like start, update and fixed_update. 

```python
#calling every instance of the game objects
from src.game_object import GameObject

for object in GameObject.INSTANCES:
    object.start()
```

```python
#Sample from variables while instantiating the game object
from src.game_object import GameObject as GO


GO.GAME_OBJECTS["katz"].Transform.rotation = 0
```