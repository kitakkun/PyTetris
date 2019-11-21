import random, copy, numpy

class Block:

    EMPTY_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    SQUARE_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    BAR_BLOCK = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    L_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    L_INVERT_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    Z_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    Z_INVERT_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    UNEVEN_BLOCK = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


    def __init__(self):
        self.block = copy.deepcopy(self.EMPTY_BLOCK)
        self.make()

    # make a new block
    def make(self):
        self.clear()
        # type = random.randint(0, 6)
        type = 1
        if type is 0:
            self.block = copy.deepcopy(self.SQUARE_BLOCK)
        elif type is 1:
            self.block = copy.deepcopy(self.BAR_BLOCK)
        elif type is 2:
            self.block = copy.deepcopy(self.L_BLOCK)
        elif type is 3:
            self.block = copy.deepcopy(self.L_INVERT_BLOCK)
        elif type is 4:
            self.block = copy.deepcopy(self.Z_BLOCK)
        elif type is 5:
            self.block = copy.deepcopy(self.Z_INVERT_BLOCK)
        elif type is 6:
            self.block = copy.deepcopy(self.UNEVEN_BLOCK)
        print(self.block)
        self.rotate()
        print(self.block)

    def rotate(self):
        tmp = numpy.array(self.block)
        for _ in range(3):
            tmp = numpy.rot90(tmp)
        tmp = tmp.tolist()
        self.block = copy.deepcopy(tmp)

    # reset block
    def clear(self):
        self.block = copy.deepcopy(self.EMPTY_BLOCK)
