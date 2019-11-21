from module.board import Board
from module.block import Block

class Tetris:
    def __init__(self):
        self.board = Board()
        self.block = Block()

    def start(self):
        pass

    def stop(self):
        pass


def main():
    tetris = Tetris()
    tetris.start()
    pass

if __name__ == '__main__':
    main()
