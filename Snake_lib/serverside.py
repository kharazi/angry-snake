'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is server code
'''
import time
import sys
import pygame
import socket
from pygame.locals import *
import worm
import food
from strtolist import datatolist
from globalvar import *


class Snake(object):

    def __init__(self):
        self.end_level = False
        self.state = 1
        self.ip = self.read_file('data/ip.txt')
        self.name = self.read_file('data/name.txt')
        print self.ip
        print self.name
       # self.option=self.read_option('data/option.csv')

        # state 1=start 2=play 3=pause 4=end

    def draw_joon(self, surface, color, x, y, i=5):
        pygame.draw.polygon(
            surface, color, ((x - i, y), (x, y + i), (x + i, y), (x, y - i)))

    def read_file(self, filename):
        File = open(filename, 'r')
        string = File.read()
        File.close()
        return string

    def run(self):
        print "run the client"
        print "and please wait to connect ... "
        HOST = self.ip
        print "Server IP :", HOST
        pygame.init()

        display = pygame.display.set_mode((500, 500))

        w = worm.Worm(display, 200, 200, 25)
        w.lag = lag
        w.head_r = 4
        w.dir_x = 0 * w.lag
        w.dir_y = -1 * w.lag
        w.first_dir_x = 0 * w.lag
        w.first_dir_y = -1 * w.lag
        w.first_dir_x, w.first_dir_y = w.dir_x, w.dir_y
        w.player_name = self.name
        w.joon = 3
        g = food.GhormeSabzi(display)
        g.r = 4

        pygame.display.set_caption("NET SNAKE")

        moket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        moket.bind((HOST, 50001))
        moket.listen(1)
        connm, addrm = moket.accept()
        print 'Connected by', addrm
        connm.send(w.player_name)
        print w.player_name + "   SENT"
        hach = connm.recv(1024)

        print hach + " RECEIVED "

        cotlet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cotlet.bind((HOST, 50002))
        cotlet.listen(1)
        connc, addrc = cotlet.accept()

        print 'Connected by', addrc
                  # Symbolic name meaning all

         # Arbitrary non-privileged
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, 50009))
        s.listen(1)
        conn, addr = s.accept()

        print 'Connected by', addr

        # print 'Connected by', addrjoon

        print "reading data..."
        font = pygame.font.Font('data/FEASFBRG.ttf', 20)
        font_h3 = pygame.font.Font('data/FEASFBRG.ttf', 60)
        text_servername = font.render(
            w.player_name, True, color_w_porrang_rect_score)
        text_client = font.render(hach, True, color_s_porrang_rect_score)
        color_text = 255, 255, 255
        text_server_win = font_h3.render(
            w.player_name + "  WIN!", True, color_w_porrang_rect_score)
        text_client_win = font_h3.render(
            hach + "  WIN!", True, color_s_porrang_rect_score)
        text_pause = font_h3.render("PAUSE", True, color_text)
        text_start = font_h3.render("PRESS SPACE...", True, color_text)

        print "data analized"
        x = (width / 2) / 2
        max_score = 10
        c = 0
        e = 80
        clientjoon = 3
        clientscore = 0
        while 1:

            c = -5
            data = ''
            while 1:

                data = conn.recv(1024)
                # connjoon.send(str(w.joon))
                conn.send(str(w.body_list))
               # data2 = conn2.recv(1024)
                # if not data: break
              #  print "hghjgh"
                break
           # print data

            # Check to :score >0
            if w.score < 0:
                w.score = 0
            if clientscore < 0:
                clientscore = 0
            # Check to :Joon<=7
            if clientjoon >= 7:
                clientjoon = 7
            if w.joon >= 7:
                w.joon = 7
            display.fill((0, 0, 0))

            ghormexoy = "&" + str(g.x) + "&" + str(g.y) + "&" + str(w.score) + "&" + str(
                w.joon) + "&" + str(clientscore) + "&" + str(clientjoon) + "&" + str(self.state) + "&"
            connc.send(ghormexoy)
            # text
            display.blit(text_servername, (x - 50, 100))
            display.blit(text_client, (width - x - 50, 100))

            pygame.draw.rect(
                display, color_w_kamrang_rect_score, (x - 50, 120, 100, 6))
            pygame.draw.rect(
                display, color_w_porrang_rect_score, (x - 50, 120, w.score * max_score, 6))

            pygame.draw.rect(
                display, color_s_kamrang_rect_score, (width - x - 50, 120, 100, 6.5))
            pygame.draw.rect(display, color_s_porrang_rect_score, (
                width - x - 50, 120, clientscore * max_score, 6.5))

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
            for i in range(w.joon):
                c += 10
                if w.joon <= 7:

                    self.draw_joon(
                        display, color_w_porrang_rect_score, x - 50 + c, y_zalamzimbo - 5)
            c = -5
            for i in range(clientjoon):
                c += 10
                if clientjoon <= 7:
                    self.draw_joon(
                        display, color_s_porrang_rect_score, width - x - 50 + c, y_zalamzimbo - 5)

            c = -5

            clientbodylist = datatolist(data)

            # barkhord ba khodesho check mikone
            for i in range(1, len(clientbodylist)):
                pygame.draw.circle(display, (0, 0, 255), (
                    clientbodylist[i][0], clientbodylist[i][1]), 4)
                if clientbodylist[0][0] == clientbodylist[i][0] and clientbodylist[0][1] == clientbodylist[i][1]:
                    print "client khord be khodesh khak to saresh"
                    clientjoon -= 1
                    clientscore -= 1

            if self.state == 2:

                if g.r + 4 > ((((g.y - clientbodylist[0][1]) ** 2) + ((g.x - clientbodylist[0][0]) ** 2)) ** (1 / 2.0)):
                    g.erase()
                    clientscore += 1
                    print "client khord"
                    g = food.GhormeSabzi(display)
                    g.r = 4
                if g.r + 4 > ((((g.y - w.y) ** 2) + ((g.x - w.x) ** 2)) ** (1 / 2.0)):
                    g.erase()
                    w.score += 1
                    print "server khord"
                    g = food.GhormeSabzi(display)
                    g.r = 4

 #               def check(self,who, x, y):
 #       if self.r+who.head_r>((((self.y-who.y)**2)+((self.x-who.x)**2))**(1/2.0)):
#            return True
 #       return False
#
            if self.state == 2:
                w.draw()

                w.move()

            if self.state == 1:
                display.blit(text_start, (width / 2 - 140, height / 2 - 50))

            if self.state == 3:
                display.blit(text_pause, (width / 2 - 70, height / 2 - 50))

            if w.score == max_score or clientjoon == 0:
                self.state = 4
                display.blit(
                    text_server_win, (width / 2 - 120, height / 2 - e))
            if clientscore == max_score or w.joon == 0:
                self.state = 4
                display.blit(
                    text_client_win, (width / 2 - 150, height / 2 - e))

            g.draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    conn.close()
         #           conn2.close()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.state == 1:
                        self.state = 2
                    elif event.key == pygame.K_SPACE and self.state == 2:
                        self.state = 3
                    elif event.key == pygame.K_SPACE and self.state == 3:
                        self.state = 2

                    if self.state == 2:
                        w.analize(event)

            time.sleep(0.01)
            pygame.display.update()

        conn.close()
        conn.close()


if __name__ == "__main__":

    mysnake = Snake()
    mysnake.run()
