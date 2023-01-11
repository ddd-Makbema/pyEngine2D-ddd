# gameEngine

A game engine built using pygame based off of the Unity game engine.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```
Initialize the screen using the init function

Initialize all the game objects you want under init in main

Load all the images you want to use into the "data" folder

Write the main game code into files in the "scripts" folder
  a sample file is provided in the script folder already
  make sure to load all the packages you want by naming the file and class name at the end of the game object declaration
  
Finally run the "main" file to run the game
## Usage

```python
import pygame

# Creates a screen to run the game on
init = Init(width, height, fps, ffps, icon, name_window)

# Creates a transformable game object onto the game screen
# This currently occurs at the top of main
GameObject(name ,screen, sprite, transform, scale, rotation, parent, packages)

# transforms the game object in user made scripts
self.game_object.transform += Vector2D(5,1)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
