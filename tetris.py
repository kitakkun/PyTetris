from module.board import Board
from module.block import Block
import sys
import pygame
import copy
from pygame.locals import *

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
            if self.can_move_down:
                self.block.y += 0.001
            else:
                self.block.y = round(self.block.y)
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
                # snap to grid
                if event.type == KEYUP:
                    if (event.key == K_LEFT) or (event.key == K_RIGHT):
                        # self.block.x = round(self.block.x)
                        pass
            self.check_block()


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
                    left = self.board.map[round(self.block.y) + y][self.block.x + x - 1]
                    right = self.board.map[round(self.block.y) + y][self.block.x + x + 1]
                    top = self.board.map[round(self.block.y) + y - 1][self.block.x + x]
                    bottom = self.board.map[round(self.block.y) + y + 1][self.block.x + x]
                    if left != 0: self.can_move_left = False
                    if right != 0: self.can_move_right = False
                    if bottom != 0: self.can_move_down = False

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
        # font = pygame.font.SysFont(None, 30)
        # debug_text = font.render("Block X:" + str(self.block.x), False, (255,255,255))
        # self.screen.blit(debug_text, [500, 500])


def main():
    tetris = Tetris()
    tetris.start()

if __name__ == '__main__':
    main()
