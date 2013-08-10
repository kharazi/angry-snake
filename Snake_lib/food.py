'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is Food(object) class & GhormeSabzi(Food) & Dombor(Food)& Joon(Food) &  Nitrogen(Food) & Nitroafzon(Food) &
'''
import pygame
import random
from globalvar import *


class Food(object):

    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(distance, surface.get_width() - distance)
        self.y = random.randint(distance, surface.get_height() - distance)
        self.color = 255, 255, 255
        self.r = 3

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.r)

    def erase(self):
        pygame.draw.circle(
            self.surface, background_color, (self.x, self.y), self.r)

    def check(self, who, x, y):
        if self.r + who.head_r > ((((self.y - who.y) ** 2) + ((self.x - who.x) ** 2)) ** (1 / 2.0)):
            return True
        return False


class GhormeSabzi(Food):

    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(distance, surface.get_width() - distance)
        self.y = random.randint(distance, surface.get_height() - distance)
        self.color = 255, 255, 255
        self.r = 3


class Dombor(Food):

    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(distance, surface.get_width() - distance)
        self.y = random.randint(distance, surface.get_height() - distance)
        self.color = 0, 0, 255
        self.r = 7


class Joon(Food):

    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(distance, surface.get_width() - distance)
        self.y = random.randint(distance, surface.get_height() - distance)
        self.color = 255, 0, 0
        self.r = 4

    def draw_joon(self, surface, color, x, y, i=5):
        pygame.draw.polygon(
            surface, color, ((x - i, y), (x, y + i), (x + i, y), (x, y - i)))

    def draw(self, surface):
        self.draw_joon(surface, self.color, self.x, self.y, self.r)

    def erase(self, surface):
        self.draw_joon(surface, background_color, self.x, self.y, self.r)


class Nitrogen(Food):

    def __init__(self, surface):
        Food.__init__(self, surface)
        self.color = 0, 255, 0
        self.r = 6


class Nitroafzon(Food):

    def __init__(self, surface):
        Food.__init__(self, surface)
        self.color = 127, 255, 200
        self.r = 6
