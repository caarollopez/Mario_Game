from object import Object


class Mountain(Object):
    """This class creates a mountain of the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        """This function is set for the sprite of the mountain"""
        return 0, 16, 120, 64, 16