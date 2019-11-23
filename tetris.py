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
            self.block.y += 0.001
            # key input
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_LEFT]:
                self.block.x -= 0.02
            if pressed_keys[K_RIGHT]:
                self.block.x += 0.02
            if pressed_keys[K_UP]:
                self.block.y -= 0.02
            if pressed_keys[K_DOWN]:
                self.block.y += 0.02
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.block.rotate()
            self.check_block()


    def stop(self):
        pass

    def get_block_real_pos(self):
        pass


    # prevent blocks from going away from game field.
    def check_block(self):
        # i: vertical(y)
        # j: horizontal(x)
        max_i = 0
        max_j = 0
        min_i = 4
        min_j = 4
        for i in range(5):
            for j in range(5):
                val = self.block.map[i][j]
                if val != 0:
                    if j <= min_j:
                        min_j = j
                    if i <= min_i:
                        min_i = i
                    if j >= max_j:
                        max_j = j
                    if i >= max_i:
                        max_i = i
        # check left wall and ground
        tmp_x = self.block.x + min_j + 1
        tmp_y = self.block.y + max_i + 1
        if tmp_x <= 1:
            self.block.x = -min_j
        if tmp_y >= self.board.v - 1:
            self.block.y = self.board.v - 2 - max_i
        # check right wall
        tmp_x = self.block.x + max_j + 1
        if tmp_x >= self.board.h - 2:
            self.block.x = self.board.h - 3 - max_j

    # write block positon into board. then make a new block
    def finalize_block(self):
        pass


    def draw(self):
        block_side_length = 30
        startX = 40
        startY = 40
        self.screen.fill((0, 0, 0))
        # draw board
        for i in range(self.board.v):
            for j in range(self.board.h):
                val = self.board.map[i][j]
                if val == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length))
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length), 2)
        # draw block
        for i in range(5):
            for j in range(5):
                val = self.block.map[i][j]
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
