'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is client code
'''
import time
import sys
import pygame
import socket
from pygame.locals import *
from strtolist import datatolist, xoyyab
from globalvar import *

import worm


class Snake(object):

    def __init__(self):
        self.end_level = False
        self.ip = self.read_file('data/ip.txt')
        self.name = self.read_file('data/name.txt')

    def draw_joon(self, surface, color, x, y, i=5):
        pygame.draw.polygon(
            surface, color, ((x - i, y), (x, y + i), (x + i, y), (x, y - i)))

    def read_file(self, filename):
        string = ''
        File = open(filename, 'r')
        string = File.read()
        return string

    def run(self):
        HOST = self.ip

        pygame.init()

        display = pygame.display.set_mode((500, 500))

        w = worm.Worm(display, 400, 400, 25)
        w.lag = lag
        w.head_r = 4
        w.dir_x = 0 * w.lag
        w.dir_y = -1 * w.lag
        w.first_dir_x, w.first_dir_y = w.dir_x, w.dir_y
        w.player_name = self.name
        w.joon = 3
        w.color = 0, 0, 255

        moket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        moket.connect((HOST, 50001))
        moket.send(w.player_name)
        print "connected"
        sss = moket.recv(1024)

        cotlet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cotlet.connect((HOST, 50002))
        print "connected"

        PORT = 50009

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print "connected"

        font = pygame.font.Font('data/FEASFBRG.ttf', 20)
        font_h3 = pygame.font.Font('data/FEASFBRG.ttf', 60)
        text_servername = font.render(
            w.player_name, True, color_w_porrang_rect_score)
        text_client = font.render(sss, True, color_s_porrang_rect_score)
        color_text = 255, 255, 255
        text_server_win = font_h3.render(
            w.player_name + "  WIN!", True, color_w_porrang_rect_score)
        text_client_win = font_h3.render(
            sss + "  WIN!", True, color_s_porrang_rect_score)
        text_pause = font_h3.render("PAUSE", True, color_text)
        text_start = font_h3.render("please wait", True, color_text)
        x = (width / 2) / 2
        max_score = 10
        c = 0
        pygame.display.set_caption("NET SNAKE")
        e = 80
        while True:
            c = -5
            s.send(str(w.body_list))
            data = s.recv(1024)

            serverbody_list = datatolist(data)
            display.fill((0, 0, 0))

            ghormexoy = cotlet.recv(1024)

            gxoy = xoyyab(ghormexoy)
            print gxoy

                       # text

            display.blit(text_client, (width - x - 50, 100))
            display.blit(text_servername, (x - 50, 100))

            pygame.draw.rect(
                display, color_w_kamrang_rect_score, (x - 50, 120, 100, 6))
            pygame.draw.rect(
                display, color_w_porrang_rect_score, (x - 50, 120, gxoy[2] * max_score, 6))

            pygame.draw.rect(
                display, color_s_kamrang_rect_score, (width - x - 50, 120, 100, 6.5))

            pygame.draw.rect(display, color_s_porrang_rect_score, (
                width - x - 50, 120, gxoy[4] * max_score, 6.5))

            state = gxoy[6]

            for i in range(7):
                c += 10
                self.draw_joon(
                    display, color_w_kamrang_rect_score, x - 50 + c, y_zalamzimbo - 5)
            c = -5

            for i in range(7):
                c += 10
                self.draw_joon(
                    display, color_s_kamrang_rect_score, width - x - 50 + c, y_zalamzimbo - 5)
            c = -5

            for i in range(gxoy[3]):
                c += 10
                if w.joon <= 7:

                    self.draw_joon(
                        display, color_w_porrang_rect_score, x - 50 + c, y_zalamzimbo - 5)
            c = -5
            for i in range(gxoy[5]):
                c += 10
                if gxoy[5] <= 7:
                    self.draw_joon(
                        display, color_s_porrang_rect_score, width - x - 50 + c, y_zalamzimbo - 5)
            c = -5

            for i in serverbody_list:

                pygame.draw.circle(display, (255, 0, 0), (i[0], i[1]), 4)

            if state == 2:
                w.draw()
                w.move()

            if state == 1:
                display.blit(text_start, (width / 2 - 140, height / 2 - 50))

            if state == 3:
                display.blit(text_pause, (width / 2 - 70, height / 2 - 50))

            pygame.draw.circle(display, (255, 255, 255), (gxoy[0], gxoy[1]), 4)

            if gxoy[2] == max_score or gxoy[5] == 0:
                display.blit(
                    text_server_win, (width / 2 - 120, height / 2 - e))
            if gxoy[4] == max_score or gxoy[3] == 0:
                display.blit(
                    text_client_win, (width / 2 - 150, height / 2 - e))

            for event in pygame.event.get():
                if event.type == QUIT:

                    s.close()
                   # s2.close()

                    pygame.quit()

                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if state == 2:
                        w.analize(event)

            pygame.display.update()
            time.sleep(0.001)


if __name__ == "__main__":

    mysnake = Snake()
    mysnake.run()
