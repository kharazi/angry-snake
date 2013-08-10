

import pygame
import pygame.font
import pygame.event
import pygame.draw
import string
from pygame.locals import *


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message):

    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (150, 0, 0), ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
        200,
        20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + string.join(current_string, ""))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
         # elif inkey == K_MINUS:
           # current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + string.join(current_string, ""))
    return string.join(current_string, "")


class input(object):

    def runserver(self):
        screen = pygame.display.set_mode((300, 100))
        result = ask(screen, "YOUR IP")
        print result
        pygame.quit()
        file = open('data/ip.txt', 'w')
        file.write(result)
        file.close()

        import serverside
        myserver = serverside.Snake()
        myserver.run()

    def runclient(self):
        screen = pygame.display.set_mode((300, 100))
        result = ask(screen, "SERVER IP")
        print result
        pygame.quit()
        file = open('data/ip.txt', 'w')
        file.write(result)
        file.close()

        import clientside
        myclient = clientside.Snake()
        myclient.run()

if __name__ == "__main__":

    myinput = input()
    myinput.run()
