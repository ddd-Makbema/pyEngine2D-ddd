"""Contains all the custom exceptions."""

class SpriteNameError(Exception):
    """Raised when the user tries to load an image not in the data folder"""
    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The sprite named {self.f} is not in the 'data' folder"
class ParentError(Exception):
    """Raised when user adds a game object that does not exist as a parent"""
    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The game object named {self.f} does not exist and is trying to be called as a parent"
        
class MultInstanceError(Exception):
    """Raised when the user tries to add multiple instances of a script to the same game object
             if the script has set that value to disallowed."""
    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The script {self.f} does not allow multiple instances to be added to the same game object."

if __name__ == '__main__':
    pass