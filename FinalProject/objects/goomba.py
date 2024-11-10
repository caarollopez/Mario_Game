from enemies import Enemy


class Goomba(Enemy):
    """This class creates the enemy Goomba of the Enemy mother class"""
    def __init__(self, x: int, y: int):
        super().__init__(x, y, direction = False)

    @property
    def sprite(self):
        """This function is set for the sprite of Goomba"""
        return 0, 32, 48, 16, 16