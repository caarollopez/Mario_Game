from object import Object


class HardBlock(Object):
    """This class creates a hard block of the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        """This function is set for the sprite of the hard block"""
        return 0, 16, 16, 16, 16
