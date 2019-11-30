from gameobject.board import Board
from gameobject.block import Block
import sys
import pygame as pg
import copy as cp
from pygame.locals import *
import math
import simpleaudio

class Tetris:

    GAME_TITLE = 'Tetris'
    can_move_left = True
    can_move_right = True
    can_move_down = True

    blue_block = pg.image.load("./image/block/blue.jpeg")
    red_block = pg.image.load("./image/block/red.jpeg")
    purple_block = pg.image.load("./image/block/purple.jpeg")
    orange_block = pg.image.load("./image/block/orange.jpeg")
    magenta_block = pg.image.load("./image/block/magenta.jpeg")
    green_block = pg.image.load("./image/block/green.jpeg")
    gray_block = pg.image.load("./image/block/gray.jpeg")

    letter_zero = pg.image.load('./image/letter/zero.png')
    letter_one = pg.image.load('./image/letter/one.png')
    letter_two = pg.image.load('./image/letter/two.png')
    letter_three = pg.image.load('./image/letter/three.png')
    letter_four = pg.image.load('./image/letter/four.png')
    letter_five = pg.image.load('./image/letter/five.png')
    letter_six = pg.image.load('./image/letter/six.png')
    letter_seven = pg.image.load('./image/letter/seven.png')
    letter_eight = pg.image.load('./image/letter/eight.png')
    letter_nine = pg.image.load('./image/letter/nine.png')

    finalized_sound_path = "./sound/block.wav"
    clearline_sound_path = "./sound/clearline.wav"

    score = 0

    def __init__(self):
        self.board = Board()
        self.block = Block()

    def start(self):
        pg.init()
        self.screen = pg.display.set_mode((700, 750))
        pg.display.set_caption(self.GAME_TITLE)
        while (True):
            self.draw()
            pg.display.update()
            if self.can_move_down or self.block.y <= round(self.block.y):
                self.block.y += 0.003
            else:
                sound = pg.mixer.Sound(self.finalized_sound_path)
                sound.play()
                self.finalize_block()
            # key input
            pressed_keys = pg.key.get_pressed()
            if pressed_keys[K_DOWN] and self.can_move_down:
                self.block.y += 0.05
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.block.rotate()
                        for x in range(5):
                            for y in range(5):
                                b_x = self.block.x + x
                                b_y = round(self.block.y) + y
                                if 0 < self.block.x + x < self.board.h - 1:
                                    val = self.board.map[b_y][b_x]
                                    if val != 0:
                                        self.block.rotate()
                                        self.block.rotate()
                                        self.block.rotate()
                    if event.key == K_LEFT and self.can_move_left:
                        self.block.x -= 1
                    if event.key == K_RIGHT and self.can_move_right:
                        self.block.x += 1
            self.check_block()
            full_lines = self.board.get_full_lines()
            if len(full_lines) > 0:
                self.score += pow(2, len(full_lines)) * 100
                print(self.score)
                sound = pg.mixer.Sound(self.clearline_sound_path)
                sound.play()
                self.board.clear_line(full_lines)


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
                    left = self.board.map[round(self.block.y) + y][self.block.x + x - 1]
                    right = self.board.map[round(self.block.y) + y][self.block.x + x + 1]
                    bottom = self.board.map[math.floor(self.block.y) + y + 1][self.block.x + x]
                    if left != 0: self.can_move_left = False
                    if right != 0: self.can_move_right = False
                    if bottom != 0: self.can_move_down = False

    # write block positon into board. then make a new block
    def finalize_block(self):
        for x in range(5):
            for y in range(5):
                val = cp.deepcopy(self.block.map[y][x])
                if val != 0:
                    self.board.map[round(self.block.y) + y][self.block.x + x] = val
        self.block.make()

    def draw(self):
        block_side_length = 30
        startX = 40
        startY = 40
        self.screen.fill((0, 0, 0))
        # draw score
        score = list(str(self.score))
        pg.draw.rect(self.screen, (0, 0, 0), Rect(500, 80, 30 * len(score), 30))
        i = 0
        for c in score:
            if c == "0":
                image = self.letter_zero
            elif c == "1":
                image = self.letter_one
            elif c == "2":
                image = self.letter_two
            elif c == "3":
                image = self.letter_three
            elif c == "4":
                image = self.letter_four
            elif c == "5":
                image = self.letter_five
            elif c == "6":
                image = self.letter_six
            elif c == "7":
                image = self.letter_seven
            elif c == "8":
                image = self.letter_eight
            elif c == "9":
                image = self.letter_nine
            self.screen.blit(image, (500 + i * 30, 80))
            i += 1
        # draw board
        for i in range(self.board.v):
            for j in range(self.board.h):
                val = self.board.map[i][j]
                if val != 0:
                    if val == 1: image = self.gray_block
                    elif val == 2: image = self.red_block
                    elif val == 3: image = self.green_block
                    elif val == 4: image = self.magenta_block
                    elif val == 5: image = self.purple_block
                    elif val == 6: image = self.blue_block
                    self.screen.blit(image, (block_side_length * j + startX, block_side_length * i + startY))
                    pg.draw.rect(self.screen, (0, 0, 0), Rect(block_side_length * j + startX, block_side_length * i + startY, block_side_length, block_side_length), 2)
        # draw block
        for i in range(5):
            for j in range(5):
                val = self.block.map[i][j]
                if val != 0:
                    if val == 2: image = self.red_block
                    elif val == 3: image = self.green_block
                    elif val == 4: image = self.magenta_block
                    elif val == 5: image = self.purple_block
                    elif val == 6: image = self.blue_block
                    self.screen.blit(image, (block_side_length * (self.block.x + j) + startX,block_side_length * (self.block.y + i) + startY,
                            block_side_length,
                            block_side_length
                        )
                    )
                    pg.draw.rect(self.screen, (0, 0, 0), Rect(
                            block_side_length * (self.block.x + j) + startX,
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
