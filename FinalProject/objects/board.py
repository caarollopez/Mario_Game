from mario import Mario
import random

# importing objects
import constants
from floor import Floor
from cloud import Cloud
from bush import Bush
from mountain import Mountain
from hard_block import HardBlock
from tuberias import Pipe

# importing special objects
from coin import Coin
from breakable_block import BreakableBlock
from question_block import QuestionBlock
from coins_block import CoinsBlock
from fire_flower import FireFlower
from mushroom import Mushroom
from star import Star

# importing enemies
from enemies import Enemy
from goomba import Goomba
from koopa import Koopa

import pyxel
import time


class Board:
    """ This class contains all the information needed to represent the game. It mainly combines every element."""

    def __init__(self, w: int, h: int, c: str):
        """This is the init method of our class Board
        @w is the width of the board
        @h is the height of the board"""
        self.width = w
        self.height = h
        self.caption = c
        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width // 2, 208, True)

        """In order to create the objects, we create lists in which we specify the object coordinates so that they can 
        be built by making for loops"""

        # main objects of the game
        # floor
        self.floor = []
        for i in range(0, constants.SCREEN_WIDTH * constants.S, 16):
            block = Floor(i, 224)
            self.floor.append(block)

        # hard blocks
        self.hard_blocks = []
        x_block = (225, 346, 378, 362, 920, 770, 786)
        y_block = (160, 180, 180, 100, 170, 208, 208)

        for i in range(len(x_block)):
            block = HardBlock(x_block[i], y_block[i])
            self.hard_blocks.append(block)

        # clouds
        self.clouds = []
        for i in range(0, constants.SCREEN_WIDTH * constants.S, 2):
            cloud = Cloud(self.width // 2, 80)
            self.clouds.append(cloud)

        # bushes
        self.bushes = []
        for i in range(0, constants.SCREEN_WIDTH * constants.S):
            bush = Bush(constants.BUSH_X, constants.BUSH_Y)
            self.bushes.append(bush)

        # mountains
        self.mountains = []
        for i in range(0, constants.SCREEN_WIDTH * constants.S):
            mountain = Mountain(constants.MOUNTAIN_X, constants.MOUNTAIN_Y)
            self.mountains.append(mountain)

        # pipes
        self.tuberias = []
        x_tub = (170, 250, 500, 610, 864)
        y_tub = 192

        for i in range(len(x_tub)):
            pipe = Pipe(x_tub[i], y_tub)
            self.tuberias.append(pipe)

        # special objects
        # we consider special objects as objects that may disappear from the screen whenever Mario touches them

        # coins
        self.coins = []
        x_coin = (754, 786, 818, 770, 802)
        y_coin = (120, 120, 120, 110, 110)

        for i in range(len(x_coin)):
            coin = Coin(x_coin[i], y_coin[i])
            self.coins.append(coin)

        # question blocks
        self.question_blocks = []
        x_question_block = (225, 346, 378, 362, 920)
        y_question_block = (160, 180, 180, 100, 170)

        for i in range(len(x_question_block)):
            block = QuestionBlock(x_question_block[i], y_question_block[i])
            self.question_blocks.append(block)

        # breakable blocks
        self.breakable_blocks = []
        x_breakable_block = (314, 330, 362, 394, 410, 680, 696, 696, 712, 712, 712, 728, 728, 728)
        y_breakable_block = (180, 180, 180, 180, 180, 180, 180, 164, 164, 164, 180, 180, 148, 164)

        for i in range(len(x_breakable_block)):
            block = BreakableBlock(x_breakable_block[i], y_breakable_block[i])
            self.breakable_blocks.append(block)

        # coins blocks
        self.coins_blocks = []
        x_coins_block = (784, 800, 816, 862, 878)
        y_coins_block = (140, 140, 140, 140, 140)

        for i in range(len(x_coins_block)):
            block = CoinsBlock(x_coins_block[i], y_coins_block[i])
            self.coins_blocks.append(block)

        # fire flower
        self.fire_flower = FireFlower(225, 144)
        # mushroom
        self.mushroom = Mushroom(346, 164)
        # star
        self.star = Star(378, 164)

        # enemies
        self.enemies = []

        # background with initial score, time
        self.coins_score = 0000000
        self.score = 0000000
        self.left_time = 500
        self.time1 = time.time()

        pyxel.init(self.width, self.height, caption=self.caption)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

        self.create_enemy()

    def create_enemy(self):
        """This method creates the enemies. There is a 25% of probability that the enemy is a Koopa Troopa and a 25% that
        the enemy is a Goomba. Also, a new enemy will be created every 100 pyxel frames, taking into account that there
        can only be a maximum of 4 enemies."""
        if pyxel.frame_count % 100 == 0 and len(self.enemies) < constants.MAX_ENEMIES:
            appearance = random.randint(1, 100)
            if appearance <= constants.KOOPA_PERCENTAGE:
                self.enemies.append(Koopa(constants.SCREEN_WIDTH, constants.KOOPA_Y))
            else:
                self.enemies.append(Goomba(constants.SCREEN_WIDTH, constants.GOOMBA_Y))


    def collision(self, objects: list):
        """This method makes Mario collide with a given list of objects.
        @objects is the list that must be provided which will contain different objects of the same type"""
        for i in range(len(objects)):
            # Checking if Mario collides from below or above with something
            # Allowing him to get on the object
            if (self.mario.y + constants.MARIO_SIZE_Y == objects[i].y) and \
                    self.mario.x in range(objects[i].x - constants.MARIO_SIZE_X - 1, objects[i].x + objects[i].sprite[3] + 1):
                self.mario.jumping = False
                self.mario.jump_counter = 0
                # this is to put mario on top of the object
                self.mario.y = objects[i].y - constants.MARIO_SIZE_Y
                return constants.COLLISION_DOWN

            # Checking if Mario is below the object
            if (self.mario.y == objects[i].y + objects[i].sprite[3]) and \
                    self.mario.x in range(objects[i].x - constants.MARIO_SIZE_X, objects[i].x + objects[i].sprite[3]):
                # if Mario collides with something above him, we make him go down as with the jump method
                self.mario.jump_counter = constants.MAX_UP_JUMP
                return constants.COLLISION_UP

            # Checking if Mario is on the corresponding coordinates that may make him collide with an object
            if (objects[i].y <= ((self.mario.y + constants.MARIO_SIZE_Y) or
                                 (self.mario.y)) <= (objects[i].y + objects[i].sprite[3])):
                # Checking either if the collision is right or left
                if pyxel.btn(pyxel.KEY_RIGHT) and (self.mario.x + constants.MARIO_SIZE_X == objects[i].x):
                    return constants.COLLISION_RIGHT
                if pyxel.btn(pyxel.KEY_LEFT) and (self.mario.x == objects[i].x + objects[i].sprite[3]):
                    return constants.COLLISION_LEFT
        return constants.NO_COLLISION



    def collisionEnemies(self, enemy: Enemy, objects: list):
        """This method allows the enemies to collide with any provided list of objects.
        @enemy is the enemy that we are checking for the collision
        @objects is the list that must be provided which will contain different objects of the same type"""
        for i in range(len(objects)):
            # Checking if the enemy collides from below with something
            # Allowing it to get on the object
            # There is an absolute value for the sprite since Koopa's sprite 3 is negative when he turns left
            if (enemy.y + enemy.sprite[4] == objects[i].y) and \
                    ((enemy.x >= objects[i].x - abs(enemy.sprite[3]) - 1) and
                     (enemy.x < objects[i].x + objects[i].sprite[3]) + 1):

                enemy.y = objects[i].y - enemy.sprite[4]
                return constants.COLLISION_DOWN

            #   Checking if the enemy is on the corresponding coordinates that may make him collide with an object
            if (objects[i].y <= ((enemy.y + enemy.sprite[4]) or (enemy.y)) <= (objects[i].y + objects[i].sprite[3])):
                # Check if the collision is either right or left, if so it will change the direction of the enemy
                if enemy.direction and (enemy.x + enemy.sprite[3] == objects[i].x):
                    enemy.change_direction()
                    return constants.COLLISION_RIGHT
                if not enemy.direction and (enemy.x == objects[i].x + objects[i].sprite[3]):
                    enemy.change_direction()
                    return constants.COLLISION_LEFT
        return constants.NO_COLLISION


    def marker(self):
        """In this method the marker from the game is being created"""
        # score
        pyxel.text(50, 6, 'MARIO', 0)
        pyxel.text(50, 16, str(self.score).zfill(5), 0)
        # coins
        pyxel.blt(90, 6, 0, 48, 104, 16, 16, colkey=0)
        pyxel.text(110, 16, 'x' + str(self.coins_score).zfill(5), 0)
        # world
        pyxel.text(150, 6, 'WORLD', 0)
        pyxel.text(150, 16, '1 - 1', 0)
        # time
        pyxel.text(200, 6, 'TIME', 0)
        self.left_time = constants.MAX_TIME - int(time.time() - self.time1)
        pyxel.text(200, 16, str(self.left_time).zfill(3), 0)

    def update(self):
        """This function is executed every frame.
        It contains all the conditions from whenever the player hits any key on the keyboard"""
        if pyxel.btnp(pyxel.KEY_Q) or self.mario.x == constants.SCREEN_WIDTH*constants.S:
            pyxel.quit()

        # COLLISIONS WITH MARIO
        pipes_collision = self.collision(self.tuberias)
        floor_collision = self.collision(self.floor)
        hard_blocks_collision = self.collision(self.hard_blocks)
        breakable_blocks_collision = self.collision(self.breakable_blocks)
        coins_blocks_collision = self.collision(self.coins_blocks)

        # right collision, left collision or down collision is a boolean which will be true if any of the following
        # conditions is happening
        right_collision = pipes_collision == constants.COLLISION_RIGHT or \
                          hard_blocks_collision == constants.COLLISION_RIGHT or \
                          breakable_blocks_collision == constants.COLLISION_RIGHT or\
                          coins_blocks_collision == constants.COLLISION_RIGHT

        left_collision = pipes_collision == constants.COLLISION_LEFT or \
                         hard_blocks_collision == constants.COLLISION_LEFT or \
                         breakable_blocks_collision == constants.COLLISION_LEFT or\
                         coins_blocks_collision == constants.COLLISION_LEFT

        down_collision = pipes_collision == constants.COLLISION_DOWN or floor_collision == constants.COLLISION_DOWN or \
                         hard_blocks_collision == constants.COLLISION_DOWN or\
                         breakable_blocks_collision == constants.COLLISION_DOWN or \
                         coins_blocks_collision == constants.COLLISION_DOWN

        # instead of creating an up collision we just create this condition
        if not down_collision and not self.mario.jumping:
            self.mario.fall()

        if pyxel.btn(pyxel.KEY_RIGHT) and not right_collision:
            self.mario.direction = True
            self.mario.move(True, self.width)

        if pyxel.btn(pyxel.KEY_LEFT) and not left_collision:
            self.mario.direction = False
            self.mario.move(False, self.width)

        if pyxel.btn(pyxel.KEY_SPACE) and down_collision:
            # this will allow mario jump only if he is colliding with something below him (so that he doesn't fly)
            self.mario.jumping = True

        if self.mario.jumping:
            self.mario.jump()

        # objects moving
        # as the same time mario goes right, the screen is moving so that it seems like mario is actually moving
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x >= self.width // 2 - constants.MARIO_SIZE_X and \
                not right_collision and not pyxel.btn(pyxel.KEY_LEFT):
            for i in range(len(self.clouds)):
                self.clouds[i].move('go')
            for i in range(len(self.floor)):
                self.floor[i].move('go')
            for i in range(len(self.bushes)):
                self.bushes[i].move('go')
            for i in range(len(self.mountains)):
                self.mountains[i].move('go')
            for i in range(len(self.coins)):
                self.coins[i].move('go')
            for i in range(len(self.tuberias)):
                self.tuberias[i].move('go')
            for i in range(len(self.hard_blocks)):
                self.hard_blocks[i].move('go')
            for i in range(len(self.breakable_blocks)):
                self.breakable_blocks[i].move('go')
            for i in range(len(self.question_blocks)):
                self.question_blocks[i].move('go')
            for i in range(len(self.coins_blocks)):
                self.coins_blocks[i].move('go')
            self.fire_flower.move('go')
            self.mushroom.move('go')
            self.star.move('go')

        # COLLISIONS WITH ENEMIES
        self.create_enemy()
        for i in range(len(self.enemies)):
            self.enemies[i].move_enemy()
            pipes_collision = self.collisionEnemies(self.enemies[i], self.tuberias)
            floor_collision = self.collisionEnemies(self.enemies[i], self.floor)
            hard_blocks_collision = self.collisionEnemies(self.enemies[i], self.hard_blocks)
            down_collision = pipes_collision == constants.COLLISION_DOWN or floor_collision == constants.COLLISION_DOWN or \
                         hard_blocks_collision == constants.COLLISION_DOWN

            if not down_collision:
                self.enemies[i].fall()

    # showing on the screen
    def draw(self):
        """This function draws graphics from the image bank"""
        pyxel.cls(6)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size

        # drawing the main objects of the game
        # floor
        for i in range(len(self.floor)):
            pyxel.blt(self.floor[i].x, self.floor[i].y, self.floor[i].sprite[0], self.floor[i].sprite[1],
                      self.floor[i].sprite[2], self.floor[i].sprite[3], self.floor[i].sprite[4])

            pyxel.blt(self.floor[i].x, self.floor[i].y + 16, self.floor[i].sprite[0], self.floor[i].sprite[1],
                      self.floor[i].sprite[2], self.floor[i].sprite[3], self.floor[i].sprite[4])

        Board.marker(self)

        # clouds
        for i in range(len(self.clouds)):
            pyxel.blt(self.clouds[i].x + 150 * i, self.clouds[i].y, self.clouds[i].sprite[0], self.clouds[i].sprite[1],
                      self.clouds[i].sprite[2],
                      self.clouds[i].sprite[3], self.clouds[i].sprite[4], colkey=13)
        # bushes
        for i in range(len(self.bushes)):
            pyxel.blt(self.bushes[i].x + 340 * i, self.bushes[i].y, self.bushes[i].sprite[0], self.bushes[i].sprite[1],
                      self.bushes[i].sprite[2],
                      self.bushes[i].sprite[3], self.bushes[i].sprite[4], colkey=12)

        # mountains
        for i in range(len(self.mountains)):
            pyxel.blt(self.mountains[i].x + 340 * i, self.mountains[i].y, self.mountains[i].sprite[0],
                      self.mountains[i].sprite[1],
                      self.mountains[i].sprite[2],
                      self.mountains[i].sprite[3], self.mountains[i].sprite[4], colkey=12)

        # hard blocks
        for i in range(len(self.hard_blocks)):
            pyxel.blt(self.hard_blocks[i].x, self.hard_blocks[i].y, self.hard_blocks[i].sprite[0],
                      self.hard_blocks[i].sprite[1],
                      self.hard_blocks[i].sprite[2], self.hard_blocks[i].sprite[3], self.hard_blocks[i].sprite[4],
                      colkey=6)

        # pipes
        for i in range(len(self.tuberias)):
            pyxel.blt(self.tuberias[i].x, self.tuberias[i].y, self.tuberias[i].sprite[0], self.tuberias[i].sprite[1],
                      self.tuberias[i].sprite[2],
                      self.tuberias[i].sprite[3], self.tuberias[i].sprite[4], colkey=6)

        # SPECIAL OBJECTS
        # coins
        for i in range(len(self.coins)):
            pyxel.blt(self.coins[i].x, self.coins[i].y, self.coins[i].sprite[0],
                      self.coins[i].sprite[1],
                      self.coins[i].sprite[2], self.coins[i].sprite[3], self.coins[i].sprite[4],
                      colkey=0)

        # breakable blocks
        for i in range(len(self.breakable_blocks)):
            pyxel.blt(self.breakable_blocks[i].x, self.breakable_blocks[i].y, self.breakable_blocks[i].sprite[0],
                      self.breakable_blocks[i].sprite[1],
                      self.breakable_blocks[i].sprite[2], self.breakable_blocks[i].sprite[3],
                      self.breakable_blocks[i].sprite[4],
                      colkey=6)

        # question blocks
        for i in range(len(self.question_blocks)):
            pyxel.blt(self.question_blocks[i].x, self.question_blocks[i].y, self.question_blocks[i].sprite[0],
                      self.question_blocks[i].sprite[1], self.question_blocks[i].sprite[2],
                      self.question_blocks[i].sprite[3], self.question_blocks[i].sprite[4], colkey=6)

        # coins blocks
        for i in range(len(self.coins_blocks)):
            pyxel.blt(self.coins_blocks[i].x, self.coins_blocks[i].y, self.coins_blocks[i].sprite[0],
                      self.coins_blocks[i].sprite[1],
                      self.coins_blocks[i].sprite[2],
                      self.coins_blocks[i].sprite[3], self.coins_blocks[i].sprite[4], colkey=6)

        # fire flower
        pyxel.blt(self.fire_flower.x, self.fire_flower.y, self.fire_flower.sprite[0], self.fire_flower.sprite[1],
                  self.fire_flower.sprite[2],self.fire_flower.sprite[3], self.fire_flower.sprite[4], colkey=6)
        # mushroom
        pyxel.blt(self.mushroom.x, self.mushroom.y, self.mushroom.sprite[0], self.mushroom.sprite[1],
                  self.mushroom.sprite[2], self.mushroom.sprite[3], self.mushroom.sprite[4], colkey=6)
        # star
        pyxel.blt(self.star.x, self.star.y, self.star.sprite[0], self.star.sprite[1], self.star.sprite[2],
                      self.star.sprite[3], self.star.sprite[4], colkey=6)

        # ENEMIES
        for i in range(len(self.enemies)):
            pyxel.blt(self.enemies[i].x, self.enemies[i].y, self.enemies[i].sprite[0], self.enemies[i].sprite[1],
                      self.enemies[i].sprite[2], self.enemies[i].sprite[3], self.enemies[i].sprite[4], colkey=6)

        # MARIO
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0], constants.MARIO_X, constants.MARIO_Y,
                  self.mario.sprite[3], self.mario.sprite[4], colkey=6)



