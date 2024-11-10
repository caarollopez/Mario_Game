from special_object import SpecialObject


class Star(SpecialObject):
    """This class creates a Star of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the star"""
        return 0, 32, 32, 16, 16