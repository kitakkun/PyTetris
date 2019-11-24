from module.board import Board
from module.block import Block
import sys
import pygame
import copy
from pygame.locals import *

class Tetris:

    GAME_TITLE = 'Tetris'

    def __init__(self):
        self.board = Board()
        self.block = Block()

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 750))
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
                # snap to grid
                if event.type == KEYUP:
                    if (event.key == K_LEFT) or (event.key == K_RIGHT):
                        self.block.x = round(self.block.x)
            self.check_block()


    def stop(self):
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
        # check left wall
        tmp_x = self.block.x + min_j + 1
        tmp_y = self.block.y + max_i + 1
        if tmp_x <= 1:
            self.block.x = -min_j
        # check right wall
        tmp_x = self.block.x + max_j + 1
        if tmp_x >= self.board.h - 2:
            self.block.x = self.board.h - 3 - max_j
        # check bottom
        if tmp_y >= self.board.v - 1:
            self.block.y = self.board.v - 2 - max_i
            # self.finalize_block()

    # write block positon into board. then make a new block
    def finalize_block(self):
        list = self.get_block_real_pos()
        for x in range(list[0], list[1]):
            for y in range(list[2], list[3]):
                self.board.map[list[6]+y][list[4]+x] = copy.deepcopy(self.block.map[y][x])


    def get_block_real_pos(self) -> list:
        min_x = 4
        min_y = 4
        max_x = 0
        max_y = 0
        # calculate where the block is
        for x in range(5):
            for y in range(5):
                tmp = self.block.map[y][x]
                if tmp != 0:
                    min_x = min(x, min_x)
                    min_y = min(y, min_y)
                    max_x = max(x, max_x)
                    max_y = max(y, max_y)
        leftmost = round(self.block.x + min_x + 1)
        topmost = round(self.block.y + min_y + 1)
        bottommost = round(self.block.y + max_y + 1)
        rightmost = round(self.block.x + max_x + 1)
        return (min_x, max_x, min_y, max_y, leftmost, rightmost, topmost, bottommost)

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

        # draw block(debug)
        startX = 500
        for i in range(5):
            for j in range(5):
                val = self.block.map[i][j]
                if val != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), Rect(
                            block_side_length * j + startX,
                            block_side_length * i + startY,
                            block_side_length,
                            block_side_length
                        )
                    )
                elif val == 0:
                    pygame.draw.rect(self.screen, (100, 100, 100), Rect(
                            block_side_length * j + startX,
                            block_side_length * i + startY,
                            block_side_length,
                            block_side_length
                        )
                    )
                pygame.draw.rect(self.screen, (0, 0, 0), Rect(
                        block_side_length * j + startX,
                        block_side_length * i + startY,
                        block_side_length,
                        block_side_length
                    )
                , 2)


def main():
    tetris = Tetris()
    tetris.start()

if __name__ == '__main__':
    main()
