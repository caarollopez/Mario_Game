from special_object import SpecialObject


class BreakableBlock(SpecialObject):
    """This class creates a breakable block of the Special Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the breakable block"""
        return 0, 0, 16, 16, 16