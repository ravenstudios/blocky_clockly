import pygame
from constants import *
import datetime
import block
import random


class Clocky():
    def __init__(self):
        self.time = datetime.datetime.now()
        self.all_blocks = [[], [], [], [], [], []]

        self.y_gap = BLOCK_SIZE * 0.2
        self.x_gap = BLOCK_SIZE * 0.2

        self.y_padding = BLOCK_SIZE // 2
        self.x_padding = 0

        self.x_spacing = BLOCK_SIZE
        self.make_clock()



    def update(self):
        self.turn_all_off()
        self.get_time()
        for block_list in self.all_blocks:
            for block in block_list:
                block.update()



    def get_time(self):
        d = datetime.datetime.now()
        th = int(d.strftime("%H")) // 10
        h = int(d.strftime("%H")) % 10
        tm = int(d.strftime("%M")) // 10
        m = int(d.strftime("%M")) % 10
        ts = int(d.strftime("%S")) // 10
        s = int(d.strftime("%S")) % 10
        all_times = [th, h, tm, m,ts, s]

        for i in range(6):
            random.shuffle(self.all_blocks[i])
            t = all_times[i]

            for j in range(t):
                self.all_blocks[i][j].is_on = True



    def turn_all_off(self):
        for block_list in self.all_blocks: #Turns all off
            for block in block_list:
                block.is_on = False



    def draw(self, surface):
        for block_list in self.all_blocks:
            for block in block_list:
                block.draw(surface)


    def make_clock(self):
        x, y, = 0, self.y_padding
        list_size = [3, 9, 6, 9, 6, 9]

        for list in range(len(self.all_blocks)):
            for i in range(list_size[list]):
                mul = list_size[list] // 3
                if i % mul == 0 and i != 0:
                    y = (BLOCK_SIZE * (i // mul)) + (self.y_gap * (i // mul)) + self.y_padding
                x = (BLOCK_SIZE * (i % mul)) + (self.x_gap * (i % mul)) + self.x_padding + self.x_spacing
                self.all_blocks[list].append(block.Block(x, y))
            self.x_spacing += (BLOCK_SIZE * mul) + (self.x_gap * mul) * 2
            y = self.y_padding
