import pyEngine2D as Engine


Engine.game_loop.init_game()	


Engine.game_loop.GO("Logo", Engine.game_loop.screen, "data/logo.png", "origin", "transform.Transform", "bounce.Bounce")
Engine.game_loop.GO.GAME_OBJECTS["Logo"].Transform.transform = [180, 240]
Engine.game_loop.GO.GAME_OBJECTS["Logo"].Transform.scale = [0.3,0.3]


Engine.game_loop.game_loop()

Engine.game_loop.quit()