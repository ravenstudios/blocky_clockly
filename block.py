import pygame
from constants import *

class Block():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.on_color = RED
        self.off_color = BLACK
        self.color = self.on_color
        self.is_on = False

    def update(self):
        self.color = self.on_color if self.is_on else self.off_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
