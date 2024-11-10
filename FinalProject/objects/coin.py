from special_object import SpecialObject


class Coin(SpecialObject):
    """This class creates a coin of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        return 0, 48, 104, 16, 16
