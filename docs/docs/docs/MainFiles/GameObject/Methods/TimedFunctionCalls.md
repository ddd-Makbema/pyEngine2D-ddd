# Timed events
All of these events happen automatically on a set timer. Almost always called from the main game loop.
## start
called before the game loop starts running. Used as a second init in case you want to make sure something is instantiated before you do something with it. 
## fixed_update
Called with eventual consistently. This means that over time the fixed_update will be called the same amount no matter (to an extent) how slow the computer running the game is. This stops a sprite from moving incredibly slow or fast because of someone's computer. <br />
This works by, every loop of the main game loop, it will check how long since the last time it reached the fixed_update method then stay in that loop until the fixed_update has caught up to where is should have been at by that point in the code when it first reached the fixed_update method. 
## update 
unlike fixed_update, this __will__ change depending on the computer's speed. It will always be called once per game loop. This can cause lag spikes if the fixed_update falls too far behind. 