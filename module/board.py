import copy

class Board:

    def __init__(self, h=12, v=21):
        self.h = h
        self.v = v
        self.map = [[0 for _ in range(h)] for _ in range(v)]
        for i in range(0, v):
            self.map[i][0] = 1
            self.map[i][h - 1] = 1
        for j in range(0, h):
            self.map[v - 1][j] = 1

    # returns full lines' vertical number
    def get_full_lines(self) -> list:
        numbers = []
        for i in range(1, self.v - 1):
            flag = True
            for j in range(1, self.h - 1):
                if self.map[i][j] is 0:
                    flag = False
            if flag is True:
                numbers.append(i)
        return numbers

    def clear_line(self, numbers: list):
        # sort(desc)
        numbers.sort()
        for number in numbers:
            for i in range(1, self.h - 1):
                self.map[number][i] = 0
            for i in range(number, 1, -1):
                for j in range(1, self.h - 1):
                    self.map[i][j] = copy.deepcopy(self.map[i - 1][j])
