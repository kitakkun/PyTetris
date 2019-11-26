import random, copy, numpy

class Block:

    EMPTY_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    SQUARE_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    BAR_BLOCK = numpy.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    L_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])

    L_INVERT_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Z_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Z_INVERT_BLOCK = numpy.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    UNEVEN_BLOCK = numpy.array([
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
        color = random.randint(2, 5)
        tmp = tmp * color
        # assign value into self.map
        self.map = copy.deepcopy(tmp.tolist())
        # rotate block some times
        rotate = random.randint(0, 3)
        for _ in range(rotate):
            self.rotate()

    def rotate(self):
        if self.can_rotate:
            self.map = self.get_rotated_map()

    def get_rotated_map(self):
        tmp = numpy.array(self.map)
        for _ in range(3):
            tmp = numpy.rot90(tmp)
        tmp = tmp.tolist()
        return tmp

    # reset block
    def clear(self):
        self.map = copy.deepcopy(self.EMPTY_BLOCK)
