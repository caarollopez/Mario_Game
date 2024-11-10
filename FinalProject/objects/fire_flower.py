from special_object import SpecialObject


class FireFlower(SpecialObject):
    """This class creates a fire flower of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the fire flower"""
        return 0, 16, 32, 16, 16