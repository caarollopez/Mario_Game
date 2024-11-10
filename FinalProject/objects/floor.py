from object import Object


class Floor(Object):
    """This class creates the floor as a child class from the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        """This function is set for the sprite of the floor"""
        return 0, 32, 104, 16, 16


