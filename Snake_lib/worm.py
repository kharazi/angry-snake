'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is Worm class(object) and AIWorm class(Worm)
'''
import pygame
from globalvar import *


class Worm(object):

    def __init__(self, surface, x, y, len=50):
        self.player_name = " "
        self.x = x
        self.y = y
        self.lag = 1
        self.first_x = self.x
        self.first_y = self.y
        self.surface = surface
        self.color = worm_color
        self.len = len
        self.body_list = [[self.x, self.y + i] for i in range(self.len)]
        self.growing = len
        self.dir_x = 0 * self.lag
        self.dir_y = -1 * self.lag
        self.first_dir_x = 0 * self.lag
        self.first_dir_y = -1 * self.lag
        self.store_dir_x = 0 * self.lag
        self.store_dir_y = 0 * self.lag

        self.joon = 3
        self.score = 0
        self.head_r = 2
        self.domborkhor = 0
        self.control_up = pygame.K_UP
        self.control_right = pygame.K_RIGHT
        self.control_down = pygame.K_DOWN
        self.control_left = pygame.K_LEFT
        self.nitrogen_key = pygame.K_RSHIFT
        self.nitrogen_counter = 2
        self.game_over = False

    def analize(self, event):

        up = self.control_up
        right = self.control_right
        down = self.control_down
        left = self.control_left
        nit = self.nitrogen_key
        if event.key == up:
            if self.dir_y == 1 * self.lag:
                return
            self.dir_x = 0 * self.lag
            self.dir_y = -1 * self.lag
        elif event.key == down:
            if self.dir_y == -1 * self.lag:
                return
            self.dir_x = 0 * self.lag
            self.dir_y = 1 * self.lag
        elif event.key == left:
            if self.dir_x == 1 * self.lag:
                return
            self.dir_x = -1 * self.lag
            self.dir_y = 0 * self.lag
        elif event.key == right:
            if self.dir_x == -1 * self.lag:
                return
            self.dir_x = 1 * self.lag
            self.dir_y = 0 * self.lag
        elif event.key == nit and self.nitrogen_counter >= 1:
            self.eat_nitrogen()
            self.nitrogen_counter -= 1

    def eat(self):
        self.growing += growing_worm

    def draw(self):
        #pygame.draw.circle(self.surface,self.color, (self.body_list[0][0],self.body_list[0][1]),self.head_r+ 1)

        for i in self.body_list:
# pygame.draw.rect(display,(255,0,0),(i[0],i[1],5,s5))
            pygame.draw.circle(
                self.surface, self.color, (i[0], i[1]), self.head_r)

    def erase(self):
        self.joon -= 1
        self.score -= 1
        self.body_list = []
        self.x = self.first_x
        self.y = self.first_y
        self.dir_x = self.first_dir_x
        self.dir_y = self.first_dir_y

    def eat_dombor(self):

        if self.domborkhor != 1:
            self.domborkhor = 1
            self.score -= 1
            self.len -= dombor_effect
            self.growing -= dombor_effect
            for i in range(dombor_effect):
                if len(self.body_list) > 20:
                    self.body_list.pop()

    def move(self):

        self.x += self.dir_x
        self.y += self.dir_y

        if self.x <= 0:
            self.x = width
        if self.y <= 0:
            self.y = height
        if self.x >= width + 1:
            self.x = 0
        if self.y >= height + 1:
            self.y = 0

        # if self.x<=-2 or self.y<=-2 or self.x>=width+1 or self.y>=height :
         #   self.erase()

        if [self.x, self.y] in self.body_list:
            self.erase()

        self.body_list.insert(0, [self.x, self.y])

        if (self.growing > self.len):
            self.len += 1

        if len(self.body_list) > self.len:
            self.body_list.pop()

    def check_to_accident(self, x, y):
        if [x, y] in self.body_list:
            return True

    def eat_nitrogen(self):
        self.store_dir_x = self.dir_x
        self.store_dir_y = self.dir_y
        self.dir_x *= 5
        self.dir_y *= 5

    def un_eat_nitrogen(self):
        self.dir_x = self.store_dir_x
        self.dir_y = self.store_dir_y
        self.store_dir_x, self.store_dir_y = 0, 0


class AIWorm(Worm):

    def __init__(self, surface, x, y, len=50):
        Worm.__init__(self, surface, x, y, len=50)
        self.start_delay = False

        self.counter = 0

    def analize(self, xekh, yekh, rival, alert, aitype):  # dlay==delay

        print aitype

        if aitype == 2:

            print self.start_delay
            if self.start_delay == True:
                self.counter += 1
            if self.start_delay == True and self.counter >= 30:
                self.counter = 0
                self.start_delay = False

            # if time==a:
            #    print "hahahhahahhhahhhahahhh\n\n\n\n\n"
            if self.start_delay == False:
                for i in rival.body_list:
                    if i[0] == self.x and abs(i[1] - self.y) < alert and self.dir_y == -1:
                        self.start_delay = True
                        if xekh >= 0:
                            self.dir_x = -1
                            self.dir_y = 0
                        if xekh < 0:
                            self.dir_x = 1
                            self.dir_y = 0

                        return
                    if i[0] == self.x and abs(i[1] - self.y) < alert and self.dir_y == 1:
                        self.start_delay = True
                        if xekh >= 0:
                            self.dir_x = -1
                            self.dir_y = 0
                        if xekh < 0:
                            self.dir_x = 1
                            self.dir_y = 0

                        return
                    if i[1] == self.y and abs(i[0] - self.x) < alert and self.dir_x == -1:
                        self.start_delay = True
                        if yekh >= 0:
                            self.dir_x = 0
                            self.dir_y = -1
                        if yekh < 0:
                            self.dir_x = 0
                            self.dir_y = 1

                        return
                    if i[1] == self.y and abs(i[0] - self.x) < alert and self.dir_x == 1:
                        self.start_delay = True
                        if yekh >= 0:
                            self.dir_x = 0
                            self.dir_y = -1
                        if yekh < 0:
                            self.dir_x = 0
                            self.dir_y = 1

                        return

                if xekh == 0:
                    if yekh < 0:
                        self.dir_x = 0
                        self.dir_y = 1
                        return
                    if yekh > 0:
                        self.dir_x = 0
                        self.dir_y = -1
                        return

                if yekh == 0:
                    if xekh < 0:
                        self.dir_x = 1
                        self.dir_y = 0
                        return
                    if xekh > 0:
                        self.dir_x = -1
                        self.dir_y = 0
                        return

                if xekh > 0:
                    if self.dir_x != 1:
                        self.dir_x = -1
                        self.dir_y = 0
                        return
                if xekh < 0:
                    if self.dir_x != -1:
                        self.dir_x = 1
                        self.dir_y = 0
                        return
                if yekh > 0:
                    if self.dir_y != 1:
                        self.dir_x = 0
                        self.dir_y = -1
                        return
                if yekh < 0:
                    if self.dir_y != -1:
                        self.dir_x = 0
                        self.dir_y = 1
                        return
        if aitype == 1:
            pass
            if xekh == 0:
                if yekh < 0:
                    self.dir_x = 0
                    self.dir_y = 1
                    return
                if yekh > 0:
                    self.dir_x = 0
                    self.dir_y = -1
                    return

            if yekh == 0:
                if xekh < 0:
                    self.dir_x = 1
                    self.dir_y = 0
                    return
                if xekh > 0:
                    self.dir_x = -1
                    self.dir_y = 0
                    return

            if xekh > 0:
                if self.dir_x != 1:
                    self.dir_x = -1
                    self.dir_y = 0
                    return
            if xekh < 0:
                if self.dir_x != -1:
                    self.dir_x = 1
                    self.dir_y = 0
                    return
            if yekh > 0:
                if self.dir_y != 1:
                    self.dir_x = 0
                    self.dir_y = -1
                    return
            if yekh < 0:
                if self.dir_y != -1:
                    self.dir_x = 0
                    self.dir_y = 1
                    return
