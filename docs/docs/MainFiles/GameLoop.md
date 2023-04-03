# Main Game Loop

The top level where the program runs. This is what is called when the game is run. <br />
## game_loop

Main function call in the whole program. Begins by calling the start method in all previously instantiated game objects. <br />
Then starts the game loop itself. The loop will follow this order<br />
1: Check if the python window has been closed and if so end the program.<br />
2: Calles fixed_update however many times is nessesary to catch up to the current time. <br />
3: Calls update once and only once. <br />
4: Waits until the time the frame should be over using the default python screen.clock.tick.
5: Adds the time the loop has taken to the timer variable to be able to call fixed update the right amount of time. 

## update
Renders the screen and calls the update function for all game objects. <br />
1: Fills the screen with a default color: currently lime green will later be able to be user defined. <br />
2: Checks if the pygame window has been closed and if so ends the program.<br />
3: calls the update method for every game object. <br />
4: Takes the transform of the game object and blits the game object onto the screen at those coords. If the transform script is not attached, then it will render it at (-1,-1) so it remains off screen. <br />
5: calls [screen.frame_end](Screen.md)

## fixed_update
Just calls the fixed update method for every game object

## delta_time
Returns the time since the function has been called last. 