from special_object import SpecialObject


class Mushroom(SpecialObject):
    """This class creates a mushroom of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the mushroom"""
        return 0, 0, 32, 16, 16