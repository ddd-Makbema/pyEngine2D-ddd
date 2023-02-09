from game_object import GameObject
import pygame

class PlayerMovement:
	def __init__(self, game_object):
		self.game_object = game_object
	def fixed_update(self):
		# self.game_object.Transform.transform = self.game_object.Transform.transform + [1,1]
		self.game_object.Transform.rotation = self.game_object.Transform.rotation -1
		# self.game_object.Transform.rotation = 45
		# self.game_object.Transform.scale = [self.game_object.Transform.scale[0] * 0.99, self.game_object.Transform.scale[1] * 0.999]
		pass
	def update(self):
		pass
if __name__ == '__main__':
    pass