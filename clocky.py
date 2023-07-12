import pygame
from constants import *
import datetime
import block
import random
class Clocky():
    def __init__(self):
        self.time = datetime.datetime.now()


        self.tenth_hours_blocks = []
        self.hours_blocks = []
        self.tenth_mins_blocks = []
        self.mins_blocks = []
        self.tenth_seconds_blocks = []
        self.seconds_blocks = []

        self.all_blocks = [
            self.tenth_hours_blocks,
            self.hours_blocks,
            self.tenth_mins_blocks,
            self.mins_blocks,
            self.tenth_seconds_blocks,
            self.seconds_blocks
        ]

        self.y_gap = BLOCK_SIZE * 0.2
        self.x_gap = BLOCK_SIZE * 0.2

        self.y_padding = BLOCK_SIZE // 2
        self.x_padding = BLOCK_SIZE

        self.x_spacing = BLOCK_SIZE
        self.make_clock()

    def update(self):
        d = datetime.datetime.now()
        print(self.time)

        th = int(d.strftime("%H")) // 10
        h = int(d.strftime("%H")) % 10
        tm = int(d.strftime("%M")) // 10
        m = int(d.strftime("%M")) % 10
        ts = int(d.strftime("%S")) // 10
        s = int(d.strftime("%S")) % 10
        print(f"{th}{h}:{tm}{m}:{ts}{s}")

        all_times = [th, h, tm, m,ts, s]

        for block_list in self.all_blocks: #Turns all off
            for block in block_list:
                block.is_on = False

        for i in range(6):
            random.shuffle(self.all_blocks[i])

            print(f"all times[{i}] {all_times[i]}")
            t = all_times[i]

            # temp = self.all_blocks[i].copy()
            for j in range(t):

                all_times[i]

                self.all_blocks[i][j].is_on = True





        for block_list in self.all_blocks:
            for block in block_list:
                block.update()

    def draw(self, surface):
        for block_list in self.all_blocks:
            for block in block_list:
                block.draw(surface)

    def make_clock(self):




        x, y, = 0, self.y_padding

        list_size = [3, 9, 6, 9, 6, 9]

        # for list in range(6):
        for i in range(3):
            y = ( i * BLOCK_SIZE) + (i * self.y_gap) + self.y_padding
            self.tenth_hours_blocks.append(block.Block(x + self.x_spacing, y))
        y = self.y_padding
        self.x_spacing += (BLOCK_SIZE * 1) + (self.x_gap * 1)


        for i in range(9):
            if i % 3 == 0 and i != 0:
                y = (BLOCK_SIZE * (i // 3)) + (self.y_gap * (i // 3)) + self.y_padding
            x = (BLOCK_SIZE * (i % 3)) + (self.x_gap * (i % 3)) + self.x_padding + self.x_spacing
            self.hours_blocks.append(block.Block(x, y))
        self.x_spacing += (BLOCK_SIZE * 3) + (self.x_gap * 3) * 2
        y = self.y_padding

        for i in range(6):
            if i % 2 == 0 and i != 0:
                y = (BLOCK_SIZE * (i // 2)) + (self.y_gap * (i // 2)) + self.y_padding
            x = (BLOCK_SIZE * (i % 2)) + (self.x_gap * (i % 2)) + self.x_padding + self.x_spacing
            self.tenth_mins_blocks.append(block.Block(x, y))
        self.x_spacing += (BLOCK_SIZE * 2) + (self.x_gap * 2) * 2
        y = self.y_padding


        for i in range(9):
            if i % 3 == 0 and i != 0:
                y = (BLOCK_SIZE * (i // 3)) + (self.y_gap * (i // 3)) + self.y_padding
            x = (BLOCK_SIZE * (i % 3)) + (self.x_gap * (i % 3)) + self.x_padding + self.x_spacing
            self.mins_blocks.append(block.Block(x, y))
        self.x_spacing += (BLOCK_SIZE * 3) + (self.x_gap * 3) * 2
        y = self.y_padding

        for i in range(6):
            if i % 2 == 0 and i != 0:
                y = (BLOCK_SIZE * (i // 2)) + (self.y_gap * (i // 2)) + self.y_padding
            x = (BLOCK_SIZE * (i % 2)) + (self.x_gap * (i % 2)) + self.x_padding + self.x_spacing
            self.tenth_seconds_blocks.append(block.Block(x, y))
        self.x_spacing += (BLOCK_SIZE * 2) + (self.x_gap * 2) * 2
        y = self.y_padding

        for i in range(9):
            if i % 3 == 0 and i != 0:
                y = (BLOCK_SIZE * (i // 3)) + (self.y_gap * (i // 3)) + self.y_padding
            x = (BLOCK_SIZE * (i % 3)) + (self.x_gap * (i % 3)) + self.x_padding + self.x_spacing
            self.seconds_blocks.append(block.Block(x, y))
        self.x_spacing += (BLOCK_SIZE * 3) + (self.x_gap * 3)

        # x = 4 * BLOCK_SIZE
