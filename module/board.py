class Board:
    def __init__(self, h=12, v=8):
        self.board = [[0 for _ in range(h)] for _ in range(v)]
        for i in range(0, v):
            self.board[i][0] = 1
            self.board[i][h - 1] = 1
        for j in range(0, h):
            self.board[v - 1][j] = 1
