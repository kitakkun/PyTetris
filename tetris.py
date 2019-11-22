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
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    print("keydown")
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT:
                        self.block.x -= 1
                    if event.key == K_RIGHT:
                        self.block.x += 1
                    if event.key == K_DOWN:
                        self.block.y += 1
                    if event.key == K_UP:
                        self.block.y -= 1


    def stop(self):
        pass

    def check_block(self):
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
                if val == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length))
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length), 2)
        # draw block
        for i in range(5):
            for j in range(5):
                val = self.block.block[i][j]
                if val != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect(
                            block_side_length * (self.block.x + 1 + j) + startX,
                            block_side_length * (self.block.y + i) + startY,
                            block_side_length,
                            block_side_length
                        )
                    )
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(
                            block_side_length * (self.block.x + 1 + j) + startX,
                            block_side_length * (self.block.y + i) + startY,
                            block_side_length,
                            block_side_length
                        )
                    , 2)

def main():
    tetris = Tetris()
    tetris.start()

if __name__ == '__main__':
    main()
