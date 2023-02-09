from game_object import GameObject as GO
from screen_init import ScreenInit
from scripts.Collider2D import CollisionHandler


screen = ScreenInit(360,480, 60, 100, "sam katz.jpg", "MyGame")
GO("collision handler", screen.screen, "null.png", "origin", "Collider2D.CollisionHandler")

GO("origin", screen.screen, "null.png", "origin", "transform.Transform")

GO("sam", screen.screen, "null.png", "origin", "transform.Transform", "Collider2D.RectangleCollider2D", "player_movement.PlayerMovement")
GO.GAME_OBJECTS["sam"].RectangleCollider2D.set_collider_size([20,20])
GO.GAME_OBJECTS["sam"].Transform.transform = [220,220]
GO.GAME_OBJECTS["sam"].Transform.scale = [1,1]
GO.GAME_OBJECTS["sam"].Transform.rotation = 0

GO("katz", screen.screen, "null.png", "origin", "transform.Transform", "Collider2D.RectangleCollider2D", "player_movement.PlayerMovement")
GO.GAME_OBJECTS["katz"].RectangleCollider2D.set_collider_size([20,20])
GO.GAME_OBJECTS["katz"].Transform.transform = [300,250]
GO.GAME_OBJECTS["katz"].Transform.scale = [1,1]
GO.GAME_OBJECTS["katz"].Transform.rotation = 0

if __name__ == '__main__':
    pass