from object import Object


class Cloud(Object):
    """This class creates a cloud of the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    @property
    def sprite(self):
        """This function is set for the sprite of the cloud"""
        return 0, 16, 64, 48, 24

