from enemies import Enemy


class Koopa(Enemy):
    """This class creates an enemy Koopa of the Enemy mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y, direction=False)


    @property
    def sprite(self):
        """This function is set for the sprite of Koopa"""
        if self.direction:
            return 0, 48, 32, 16, 24
        else:
            return 0, 48, 32, -16, 24


