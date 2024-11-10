import constants


class Mario:
    def __init__(self, x: int, y: int, direction: bool):
        """This function is used to initialize Mario
        @x is mario's x coordinate
        @y is mario's y coordinate
        @direction is mario's direction, where true means right, false means left"""
        self.x = x
        self.y = y
        self.died = False
        self.direction = direction
        self.jump_counter = 0
        self.jumping = False
        self.lives = 3


    @property
    def sprite(self):
        """This function is set for the sprite of Mario"""
        # SELF SPRITE: image bank, starting x, starting y, size (width x height)
        if self.direction:
            return 0, constants.MARIO_X, constants.MARIO_Y, constants.MARIO_SIZE_X, constants.MARIO_SIZE_Y
        else:
            return 0, constants.MARIO_X, constants.MARIO_Y, -constants.MARIO_SIZE_X, constants.MARIO_SIZE_Y

    @property
    def x(self):
        """It gets Mario's x coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """It checks Mario's x coordinate, raising errors when considered"""
        if type(x) != int:
            raise TypeError("It should be an integer")
        elif x >= 0:
            self.__x = x
        else:
            raise ValueError("Out of the screen")

    @property
    def y(self):
        """It gets Mario's y coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        """It checks Mario's y coordinate, raising errors when considered"""
        if type(y) != int:
            raise TypeError("It should be an integer")
        elif y >= 0:
            self.__y = y
        else:
            raise ValueError("Out of the screen")

    @property
    def direction(self):
        """It gets Mario's direction, which is a boolean. True means right and False means left"""
        return self.__direction

    @direction.setter
    def direction(self, direction):
        """It checks Mario's direction, raising errors when considered"""
        if type(direction) != bool:
            raise TypeError("It should be a boolean")
        else:
            self.__direction = direction


    def move(self, direction: bool, size: int):
        """This function allows mario to move right or left
        @direction is the parameter for mario's direction (right means true and left means false)
        @size is the screen's width
        """
        mario_x_size = self.sprite[3]
        if direction and self.x < ((size//2) - mario_x_size):
            self.x += 1
        elif not direction and self.x > 0:
            self.x -= 1


    @property
    def jump_counter(self):
        """It gets Mario's jump counter; that is the counter that determines the status of the jump"""
        return self.__jump_counter

    @jump_counter.setter
    def jump_counter(self, jump_counter: int):
        """It sets the jump counter, checking its values and raising errors if necessary
        @jump_counter states the moment at which Mario is of the jump"""
        if type(jump_counter) != int:
            raise TypeError("jump_counter must be an int")
        # Here I need to consider jump_counter again as if it were private
        elif jump_counter < 0:
            raise ValueError("jump_counter must be not equal to 0")
        else:
            self.__jump_counter = jump_counter

    @property
    def jumping(self):
        """It gets Mario's jumping"""
        return self.__jump_counter

    @jumping.setter
    def jumping(self, jump_counter: bool):
        """It sets Mario's jumping
        @jumping determines whether Mario is jumping (True) or not(False)"""
        if type(jump_counter) != bool:
            raise TypeError("jumping must be a boolean")
        else:
            self.__jump_counter = jump_counter

    def jump(self):
        """This function allows mario to jump by using the previous attributes that were defined"""
        if self.jump_counter < constants.MAX_UP_JUMP:
            self.jump_counter += 1
            self.y -= 2

        elif self.jump_counter < constants.MAX_JUMP_COUNTER:
            self.jump_counter += 1
            self.fall()

        else:
            self.jump_counter = 0
            self.jumping = False

    def fall(self):
        """This method makes Mario go down whenever it is necessary. It will mainly be when he is not on a block
        anymore """
        self.y += 2

    @property
    def lives(self):
        """It get the lives of Mario"""
        return self.__lives

    @lives.setter
    def lives(self, lives):
        """It check the lives of Mario, raising the corresponding errors
        @lives are the actual lives of Mario"""
        if type(lives) != int:
            raise TypeError("It should be an integer")
        elif lives > constants.LIVES:
            raise ValueError("Mario can't have more than 3 lives")
        elif lives <= 0:
            raise ValueError("Mario is dead, he has not lives")
        else:
            self.__lives = lives





