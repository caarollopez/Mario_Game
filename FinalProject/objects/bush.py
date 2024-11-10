from object import Object


class Bush(Object):
    """This class creates a bush of the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        """This function is set for the sprite of the bush"""
        return 0, 16, 88, 48, 16