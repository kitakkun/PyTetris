from gameobject.board import Board
from gameobject.block import Block
import sys
import pygame
import copy
from pygame.locals import *
import math

class Tetris:

    GAME_TITLE = 'Tetris'
    can_move_left = True
    can_move_right = True
    can_move_down = True

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
            if self.can_move_down or self.block.y <= round(self.block.y):
                self.block.y += 0.001
            else:
                self.finalize_block()
            # key input
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_DOWN] and self.can_move_down:
                self.block.y += 0.02
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.block.rotate()
                    if event.key == K_LEFT and self.can_move_left:
                        self.block.x -= 1
                    if event.key == K_RIGHT and self.can_move_right:
                        self.block.x += 1
            self.check_block()
            self.board.clear_line(self.board.get_full_lines())


    def stop(self):
        pass

    # prevent blocks from going away from game field.
    def check_block(self):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        for x in range(5):
            for y in range(5):
                val = self.block.map[y][x]
                if val != 0:
                    left_x = self.block.x + x - 1
                    right_x = self.block.x + x + 1
                    bottom_y = math.floor(self.block.y) + y + 1
                    if left_x <= 0:
                        self.block.x = 1 - x
                    if right_x >= self.board.h - 1:
                        self.block.x = self.board.h - 2 - x
                    left = self.board.map[math.floor(self.block.y) + y][self.block.x + x - 1]
                    right = self.board.map[math.floor(self.block.y) + y][self.block.x + x + 1]
                    top = self.board.map[math.floor(self.block.y) + y - 1][self.block.x + x]
                    bottom = self.board.map[math.floor(self.block.y) + y + 1][self.block.x + x]
                    if left != 0: self.can_move_left = False
                    if right != 0: self.can_move_right = False
                    if bottom != 0: self.can_move_down = False

    # write block positon into board. then make a new block
    def finalize_block(self):
        for x in range(5):
            for y in range(5):
                val = copy.deepcopy(self.block.map[y][x])
                if val != 0:
                    self.board.map[round(self.block.y) + y][self.block.x + x] = val
        self.block.make()

    def draw(self):
        block_side_length = 30
        startX = 40
        startY = 40
        self.screen.fill((0, 0, 0))
        # draw board
        for i in range(self.board.v):
            for j in range(self.board.h):
                val = self.board.map[i][j]
                if val != 0:
                    if val == 1:
                        color = pygame.color.Color(255, 255, 255)
                    if val == 2:
                        color = pygame.color.Color(100, 150, 100)
                    elif val == 3:
                        color = pygame.color.Color(255, 100, 100)
                    elif val == 4:
                        color = pygame.color.Color(100, 255, 100)
                    elif val == 5:
                        color = pygame.color.Color(100, 100, 255)
                    else:
                        color = pygame.color.Color(255, 255, 255)
                    pygame.draw.rect(self.screen, color, Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length))
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length), 2)
        # draw block
        for i in range(5):
            for j in range(5):
                val = self.block.map[i][j]
                if val != 0:
                    if val == 2:
                        color = pygame.color.Color(100, 150, 100)
                    elif val == 3:
                        color = pygame.color.Color(255, 100, 100)
                    elif val == 4:
                        color = pygame.color.Color(100, 255, 100)
                    elif val == 5:
                        color = pygame.color.Color(100, 100, 255)
                    else:
                        color = pygame.color.Color(255, 255, 255)
                    pygame.draw.rect(self.screen, color, Rect(
                            block_side_length * (self.block.x + j) + startX,
                            block_side_length * (self.block.y + i) + startY,
                            block_side_length,
                            block_side_length
                        )
                    )
                    pygame.draw.rect(self.screen, (0, 0, 0), Rect(
                            block_side_length * (self.block.x + j) + startX,
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