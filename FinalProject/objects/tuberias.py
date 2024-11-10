from object import Object


class Pipe(Object):
    """This class creates a Pipe of the Object mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


    @property
    def sprite(self):
        return 0, 32, 0, 32, 32