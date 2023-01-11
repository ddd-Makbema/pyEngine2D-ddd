from game_object import GameObject
from data_types import Vector2D

class Transform:
	def __init__(self, game_object, transform, scale, rotation):
		self.game_object = game_object
        self.transform = transform 
		self.scale = scale
		self.rotation = rotation
    	self.last_scale = None
		self.last_parent_scale = None

    def start():
        self.size = Vector2D(self.image_start.get_width(), self.image_start.get_height())
    
    def update():
        self.load = self._f_scale()
    
    def parent_transform(self):
		"""Returns the transform of the gameObject to local coords translated from the parent object. If there isn't a parent then returns normal coords."""
	
		if not self.parent:
			return (self.transform.x,self.transform.y)
		else:		
			rotate_trans = self._rotate_transform(self.parent_instance.rotation, 
				self.transform.x*self.parent_instance.scale.x, self.transform.y*self.parent_instance.scale.y)
			return rotate_trans
			
	def _scale(self):
		"""Scales the game object's pixels according to the scale number and the parent's scale number and returns it."""
		
		if not self.parent:
			if self.scale != self.last_scale:
				self.last_scale = self.scale
				scale = (self.scale.x * self.size.x, self.scale.y * self.size.y)
				self.previous_scale = scale
				return scale
			return self.previous_scale
		elif self.parent_instance.scale != self.last_parent_scale or self.scale != self.last_scale:
			p_scale = self._parent_scale()
			return p_scale
		return self.previous_scale

	def _parent_scale(self):
		"""scales the object according to the parent's scale value"""

		self.last_scale = self.scale
		self.last_parent_scale = self.parent_instance.scale
		p_scale = (self.scale.x * self.size.x * self.parent_instance.scale.x,
					self.scale.y * self.size.y * self.parent_instance.scale.y)
		self.previous_scale = p_scale
		return p_scale

	def _rotate_transform(self, rotation, radius_x, radius_y):
		"""Transforms the child to account for the parent's rotation"""

		angle_rad = math.radians(180-rotation)
		x = radius_x * math.sin(angle_rad)
		y = radius_y * math.cos(angle_rad)
		return (x+self.parent_instance.transform.x,y+self.parent_instance.transform.y)

	def _f_scale(self):
		"""Scales the image accounting for parent/child transforms
  and returns the image to be rendered."""

		scale = self._scale()
		image = pygame.transform.scale(self.image_start , scale)

		if self.parent:
			image = pygame.transform.rotate(image, self.rotation-self.parent_instance.rotation)
		else:
			image = pygame.transform.rotate(image, -self.rotation)
		return image
