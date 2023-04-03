# Package Method Calls

## Collisions

### on_collision

Only called if both game objects have [is_trigger]() set to false. <br />
Will stop the game objects from phasing through each other once they start to collide. <br />
Will pass in __other__ which is the other game object in that collision.

#### Enter
Called on both game objects involved in a collision, only on the physics frame that they start to collide. 
#### Stay
Same as enter, called each physics frame that the two game objects stay together.
#### Exit
same as enter, called on the physics frame that the game objects stop touching.

### on trigger
Only called if __one__ of the game obejcts in the collision has  [is_trigger]() set to true. If both colliders have it set to true, then nothing happens.<br />
This will not stop the game objects from going through each other. <br />
Will pass in __other__ which is the other game object in that collision.
<br /><br />
On trigger has the same 3 methods as on collision just as "on_trigger_enter" not "on_collision_enter"

