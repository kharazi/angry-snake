'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is Wall class
'''
import pygame
from globalvar import *


class Wall(object):

    def __init__(self, display):
        self.display = display
        self.x = 0
        self.y = 0
        self.wall_size_w = width / mapw
        self.wall_size_h = height / maph
        self.border = []
        self.color = wall_color

    def draw(self):
        pygame.draw.rect(self.display, self.color, (
            self.x, self.y, self.wall_size_w, self.wall_size_h))

    def set_border(self):
        i = 0
        while i <= self.wall_size_w:
            self.border.append([self.x + i, self.y])
            i += 1
        j = 0
        while j <= self.wall_size_h:
            self.border.append([self.x, self.y + j])
            j += 1
        k = 0
        while k <= self.wall_size_w:
            self.border.append([self.x + k, self.y + self.wall_size_h])
            k += 1
        h = 0
        while h <= self.wall_size_h:
            self.border.append([self.x + self.wall_size_w, self.y + h])
            h += 1

    def check(self, x, y):
        if [x, y] in self.border:
            return True
