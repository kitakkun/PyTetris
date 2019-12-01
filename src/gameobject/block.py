import random
import numpy as np
import copy as cp

class Block:

    EMPTY_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    SQUARE_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    BAR_BLOCK = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    L_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])

    L_INVERT_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Z_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Z_INVERT_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    UNEVEN_BLOCK = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    def __init__(self):
        self.x = 4
        self.y = 0
        self.make()

    # make a new block
    def make(self):
        self.clear()
        self.x = 4
        self.y = 0
        self.can_rotate = True
        type = random.randint(0, 6)
        if type is 0:
            tmp = self.SQUARE_BLOCK
            self.can_rotate = False
        elif type is 1:
            tmp = self.BAR_BLOCK
        elif type is 2:
            tmp = self.L_BLOCK
        elif type is 3:
            tmp = self.L_INVERT_BLOCK
        elif type is 4:
            tmp = self.Z_BLOCK
        elif type is 5:
            tmp = self.Z_INVERT_BLOCK
        elif type is 6:
            tmp = self.UNEVEN_BLOCK
        # determine the block's color
        color = random.randint(2, 6)
        tmp = tmp * color
        # assign value into self.map
        self.map = cp.deepcopy(tmp.tolist())
        # rotate block some times
        rotate = random.randint(0, 3)
        for _ in range(rotate):
            self.rotate()
        # adjust y position
        min_y = 4
        for x in range(5):
            for y in range(5):
                if self.map[y][x] != 0:
                    min_y = min(min_y, y)
        self.y = - min_y

    def rotate(self):
        if self.can_rotate:
            self.map = self.get_rotated_map()

    def get_rotated_map(self):
        tmp = np.array(self.map)
        for _ in range(3):
            tmp = np.rot90(tmp)
        tmp = tmp.tolist()
        return tmp

    # reset block
    def clear(self):
        self.map = cp.deepcopy(self.EMPTY_BLOCK)
