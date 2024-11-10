class Enemy:
    """This class creates the different enemies of the game"""
    def __init__(self, x: int, y: int, direction: bool):
        self.x = x
        self.y = y
        self.direction = direction

    def move_enemy(self):
        """This method allows the enemy to move, taking its direction into account"""
        if self.direction:
            self.x += 1
        elif not self.direction:
            self.x -= 1

    def change_direction(self):
        """This method changes the direction of the corresponding enemy"""
        self.direction = not self.direction

    def fall(self):
        """This function makes the enemies fall down"""
        self.y += 2
