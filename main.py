import pygame
import sys
from pygame.locals import *
import pygame_menu
import os

# inicjacja modułu pygame
pygame.init()

szerokosc = 800
wysokosc = 600
#szerokosc okna
oknogry = pygame.display.set_mode((szerokosc, wysokosc), 0, 32)

#wstawiamy obrazek
background = pygame.image.load("image/download.jfif")
background = pygame.transform.scale(background, (szerokosc, wysokosc))

#pobieranie informacji o image
screen = pygame.display.get_surface()
#rozmieszczenie zdjecia
screen.blit(background,(0,0))
pygame.display.flip()


# tytuł okna
pygame.display.set_caption("Pong")

'''
class mainBackgammonGame():
    szerokosc = 800
    wysokosc = 600
    def __init__(self):
        self.oknogry = pygame.display.set_mode((szerokosc, wysokosc), 0, 32)
        pygame.display.set_caption("Pong")

def start_the_game():
    oknogry2 = pygame.display.set_mode((szerokosc, wysokosc), 0, 32)
    background = pygame.image.load("image/download.jfif")
    background = pygame.transform.scale(background, (szerokosc, wysokosc))
    screen = pygame.display.get_surface()
#rozmieszczenie zdjecia
    screen.blit(background,(0,0))
    pygame.display.flip()
    pass       

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(oknogry)
'''

while True:
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #wyswietlenie okna
    pygame.display.update()