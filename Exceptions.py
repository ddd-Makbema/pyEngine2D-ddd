"""Contains all the custom exceptions."""

class SpriteNameError(Exception):
    """Raised when the user tries to load an image not in the data folder"""
    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The sprite named {self.f} is not in the 'data' folder"