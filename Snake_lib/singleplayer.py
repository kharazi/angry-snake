'''
Copyright 1390(2012(AD)) Vahid Kharazi <kharazi72@gmail.com>
Licensed for distribution under the GPL version 3
This is one player
'''
#
# IMPORT
import time
import sys
import pygame
from pygame.locals import *
from globalvar import *
import wall
import worm
import food
import slidemenu
#


class Snake(object):

    def __init__(self):
        self.end_level = False
        self.joon_show = False
        self.start_j_time = 0
        self.show_nitrogen = False
        self.start_n_time = 0
        self.start_eat_n = 0
        self.time = 0
        self.step = 0.01
        self.option = self.read_option('data/option.csv')
        self.map = self.read_map('data/map/level2.txt')
        self.level = 2
        self.state = "start"
    #-------------------------------------------------------------------------

    def read_map(self, filename):
        c = self.option[8][0]
        map = []
        File = open(filename, 'r')
        line_count = 0
        char_count = 0
        for line in File:
            char_count = 0
            line_count += 1
            for char in line:
                char_count += 1
                if char == c:
                    map .append([char_count, line_count])
        File.close()
        return map
    #-------------------------------------------------------------------------

    def read_option(self, filename):
        option = []
        File = open(filename, 'r')
        for line in File:
            l = line.split(',')
            del l[0]
            option.append(l)

        return option

    def write_log(self, text):
        file = open('data/log.csv', 'a')
        file.write(text)
        file.close()

    def draw_joon(self, surface, color, x, y, i=5):
        pygame.draw.polygon(
            surface, color, ((x - i, y), (x, y + i), (x + i, y), (x, y - i)))
    #-------------------------------------------------------------------------

    def run(self):
        max_score = int(self.option[9][0])
        pygame.init()
        # SET DISPLAY
        global ghorme_counter
        display = pygame.display.set_mode((width, height))
        title = ""
        for i in range(len(self.option[5])):
            title += self.option[5][i] + " "
        pygame.display.set_caption(title)

        # WALL
        walla = []
        for i in self.map:
            walak = wall.Wall(display)
            walak.x = (i[0] - 1) * (width / mapw)
            walak.y = (i[1] - 1) * (height / maph)
            walak.set_border()
            walla.append(walak)

        # OBJECT
        #----------------------------------------------------------------------
        # WORM1
        #----------------------------------------------------------------------
        w = worm.Worm(display, int(self.option[12][0]), int(
            self.option[12][1]), int(self.option[10][0]))
        w.first_dir_x, w.first_dir_y = w.dir_x, w.dir_y
        w.player_name = self.option[0][0]
        w.joon = int(self.option[6][0])

        #----------------------------------------------------------------------
        # FOODS
        #----------------------------------------------------------------------
        g = food.GhormeSabzi(display)
        j = food.Joon(display)
        n = food.Nitrogen(display)
        d = food.Dombor(display)
        na = food.Nitroafzon(display)
        #----------------------------------------------------------------------
        # TEXT
        #----------------------------------------------------------------------
       # font= pygame.font.SysFont(name="Feast of Flesh BB",size= 20)
        #font_h3= pygame.font.SysFont(name="Feast of Flesh BB",size= 60)
        font = pygame.font.Font('data/FEASFBRG.ttf', 20)
        font_h3 = pygame.font.Font('data/FEASFBRG.ttf', 60)
       # dg=pygame.font.Font()
        color_text = int(self.option[7][0]), int(
            self.option[7][1]), int(self.option[7][2])
        #w.color)
        text_player1 = font.render(
            w.player_name, True, color_w_porrang_rect_score)

        text_player_w_win = font_h3.render("YOU  WIN!", True, color_text)
        text_player_w_lose = font_h3.render("YOU LOSE!", True, color_text)
        text_pause = font_h3.render("PAUSE", True, color_text)
        text_start = font_h3.render("PRESS SPACE...", True, color_text)

        #----------------------------------------------------------------------
        # MUSIC
        #----------------------------------------------------------------------
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        background_music = pygame.mixer.Sound('data/sound/background.ogg')
        todifar_music = pygame.mixer.Sound('data/sound/todifar.ogg')
        tnt_music = pygame.mixer.Sound('data/sound/tnt.ogg')
        eat_music = pygame.mixer.Sound('data/sound/eat.wav')

        # SET VOLUME
        background_music.set_volume(float(self.option[3][0]))
        todifar_music.set_volume(float(self.option[4][0]))
        tnt_music .set_volume(float(self.option[4][0]))
        eat_music.set_volume(float(self.option[4][0]))

        background_music.play(-1)
        #----------------------------------------------------------------------

        c = 0
        x = (width / 2) / 2
        e = 80
        tt = 0

        while True:

            c = -5
            # The time of game
            self.time += self.step
            # Check to :score >0
            if w.score < 0:
                w.score = 0
            # Check to :Joon<=7
            if w.joon >= 7:
                w.joon = 7

            display.fill(background_color)

            if w.joon < 0:

                w.game_over = True
                self.end_level = True
            # play sound
                display.blit(
                    text_player_w_lose, (width / 2 - 120, height / 2 - e))
                if tt == 0:
                    self.write_log('\n' + '1player' + ',' + str(
                        self.level) + ',' + ' ' + ',' + ' ' + ',' + w.player_name + ',' + str(w.score))
                tt += 1
            if w.score == max_score:
                self.end_level = True
                display.blit(
                    text_player_w_win, (width / 2 - 120, height / 2 - e))
                if tt == 0:
                    self.write_log('\n' + '1player' + ',' + str(
                        self.level) + ',' + w.player_name + ',' + str(w.score) + ',' + ' ' + ',' + ' ')
                tt += 1
            if self.end_level:
                self.state = "EndLevel"

            # USER FREINDLY
            #-----------------------------------------------------------
            display.blit(text_player1, (x - 50, 100))

            pygame.draw.rect(
                display, color_w_kamrang_rect_score, (x - 50, 120, 100, 6))

            pygame.draw.rect(
                display, color_w_porrang_rect_score, (x - 50, 120, w.score * max_score, 6))

            pygame.draw.polygon(display, color_w_porrang_rect_score, (
                (x - 50 + e, y_zalamzimbo - 10), (x - 40 + e, y_zalamzimbo), (x - 50 + e, y_zalamzimbo)))
            pygame.draw.polygon(display, color_w_porrang_rect_score, (
                (x - 40 + e, y_zalamzimbo - 10), (x - 30 + e, y_zalamzimbo), (x - 40 + e, y_zalamzimbo)))

            if w.nitrogen_counter == 0:
                pygame.draw.polygon(display, color_w_kamrang_rect_score, (
                    (x - 50 + e, y_zalamzimbo - 10), (x - 40 + e, y_zalamzimbo), (x - 50 + e, y_zalamzimbo)))
                pygame.draw.polygon(display, color_w_kamrang_rect_score, (
                    (x - 40 + e, y_zalamzimbo - 10), (x - 30 + e, y_zalamzimbo), (x - 40 + e, y_zalamzimbo)))

            if w.nitrogen_counter == 1:
                pygame.draw.polygon(display, color_w_kamrang_rect_score, (
                    (x - 40 + e, y_zalamzimbo - 10), (x - 30 + e, y_zalamzimbo), (x - 40 + e, y_zalamzimbo)))

            for i in range(7):
                c += 10
                self.draw_joon(
                    display, color_w_kamrang_rect_score, x - 50 + c, y_zalamzimbo - 5)
            c = -5

            for i in range(w.joon):
                c += 10
                if w.joon <= 7:

                    self.draw_joon(
                        display, color_w_porrang_rect_score, x - 50 + c, y_zalamzimbo - 5)
            c = -5

            #------------------------------------------------------------------

            #DRAWING & MOVEING
            w.draw()
            if self.state == "play":
                w.move()

                        # Draw wall & check worms to accident
            for i in walla:
                i.draw()
            for i in walla:
                if i.check(w.x, w.y):
                    w.erase()
                    todifar_music.play(1)
                    break

            # Event
            # FOOD
            #------------------------------------------
            # Ghorme Sabzi
            #------------------------------------------
            if ghorme_counter < max_of_ghorme:
                g.draw()
            if g.check(w, w.x, w.y):
                w.score += 1
                w.eat()
                eat_music.play()
                ghorme_counter += 1
                if ghorme_counter < max_of_ghorme:
                    g = food.GhormeSabzi(display)

            if ghorme_counter == max_of_ghorme:
                # ino badan bezaram True bazi ba tamom shodan ghorme sabziya
                # tamom mishe va
                self.end_level = False
            #------------------------------------------

            #------------------------------------------
            # jooooooon
            #------------------------------------------
            if self.time % 10.0 < 0.01:
                self.joon_show = True
                self.start_j_time = self.time

            if self.time > (self.start_j_time + 8.0):
                self.joon_show = False

            if self.joon_show:
                j.draw(display)
            else:
                j.erase(display)
            if j.check(w, w.x, w.y):
                w.joon += 1
                j.erase(display)
                eat_music.play()
                j = food.Joon(display)

            #-------------------------------------------
            # Nitrogen
            #-------------------------------------------
            n.draw()
            if self.time >= 7and self.time % 7.0 < 0.01:
                self.show_nitrogen = True
            #    print "hfghfg"
                self.start_n_time = self.time
                n.draw()

            if n.check(w, w.x, w.y):
                n.erase()
                eat_music.play()
                self.start_eat_n = self.time
                n = food.Nitrogen(display)
                w.eat_nitrogen()
                if self.time == self.start_eat_n + 0.1:
                    w.un_eat_nitrogen()

            #---------------------------------------

            #-------------------------------------------
            # Dombor
            #-------------------------------------------
            if ghorme_counter > 0 and ghorme_counter % 2 == 0:
                d.draw()

                if d.check(w, w.x, w.y):
                    w.eat_dombor()
                    d.erase()
                    eat_music.play()

            #--------------------------------------------
            # Nitro Afzon
            #--------------------------------------------
            na.draw()
            if na.check(w, w.x, w.y):
                w.score += 1
                eat_music.play()
                if w.nitrogen_counter < 2:
                    w.nitrogen_counter += 1
                na = food.Nitroafzon(display)

            #--------------------------------------------------
            # Check Event
            #--------------------------------------------------

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.state == "start":
                        self.state = "play"
                    elif event.key == pygame.K_SPACE and self.state == "play":
                        self.state = "pause"
                    elif event.key == pygame.K_SPACE and self.state == "pause":
                        self.state = "play"

                    if self.state == "play":
                        w.analize(event)

            if self.state == "start":
                display.blit(text_start, (width / 2 - 140, height / 2 - 50))

            if self.state == "pause":
                display.blit(text_pause, (width / 2 - 70, height / 2 - 50))

            pygame.display.update()
            time.sleep(self.step)
       #     print self.state

            if self.state == "EndLevel":
                background_music.stop()
               # print "THE END"


           # if self.state=='EndLevel':
            #    background_music.stop()
              #   level3=Snake()
                # level3.map=level3.read_map('data/map/level3.txt')
               # level3.run()
if __name__ == "__main__":

    mysnake = Snake()
    mysnake.run()
