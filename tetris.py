from module.board import Board
from module.block import Block
import sys
import pygame
from pygame.locals import *

class Tetris:

    GAME_TITLE = 'Tetris'

    def __init__(self):
        self.board = Board()
        self.block = Block()
        self.start()

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 750))
        pygame.display.set_caption(self.GAME_TITLE)
        while (True):
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type is QUIT:
                    pygame.quit()
                    sys.exit()


    def stop(self):
        pass

    def draw(self):
        block_side_length = 30
        startX = 40
        startY = 40
        self.screen.fill((0, 0, 0))
        # draw board
        for i in range(self.board.v):
            for j in range(self.board.h):
                val = self.board.board[i][j]
                if val is 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length))
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length), 2)
        # draw block
        pygame.draw.rect(self.screen, (255, 255, 255), Rect(
                block_side_length * (self.block.x + 1) + startX,
                block_side_length * self.block.y + startY,
                block_side_length,
                block_side_length
            )
        )
        pygame.draw.rect(self.screen, (0, 0, 0), Rect(
                block_side_length * (self.block.x + 1) + startX,
                block_side_length * self.block.y + startY,
                block_side_length,
                block_side_length
            )
        , 2)

def main():
    tetris = Tetris()
    tetris.start()

if __name__ == '__main__':
    main()
