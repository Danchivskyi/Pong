# coding=utf-8

import pygame
import pygame.locals
import sys
import main
from pygame import mouse

PAUZA=0
width = 800
height = 400
class Plansza(object):

    def __init__(self, width, height):
        """
        Konstruktor
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Gra Pong 3EF-DI')

    def draw(self, *args):
        """
        rysowanie okna gry
        """
        global PAUZA
        #background = (0,0,0)
        background = pygame.image.load("img/tlo.png")
        self.surface.blit(background, (0,0))
        #background = (230, 255, 255)
        #self.surface.fill(background)
        if(PAUZA==0):
            for Rysuj in args:
                Rysuj.draw_on(self.surface)

            # dopiero w tym miejscu następuje fatyczne rysowanie
            # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
            pygame.display.update()
        elif(PAUZA==1):
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 330 <= mouse[0] <= 330 + 140 and height / 2 - 50 <= mouse[1] <= height / 2 - 10:
                        PAUZA=0
                    if 330 <= mouse[0] <= 330 + 140 and height / 2 +10  <= mouse[1] <= height / 2 + 50:
                        PAUZA=0
                        main.main()
                        #pygame_menu.menu()
                        #pygame.quit()
                    if 330 <= mouse[0] <= 330 + 140 and height / 2 +70  <= mouse[1] <= height / 2 + 110:
                        pygame.quit()
                        #pygame_menu.menu()
                        #pygame.quit()

            pauza = pygame.font.SysFont('Consolas', 32).render('Pauza', True, pygame.color.Color('White'))
            self.surface.blit(pauza, (350, 80))
            #pygame.draw.rect(self.surface, (170,0,0), [width / 2, height / 2, 140, 40])
            graj = pygame.image.load("img/play.png")
            self.surface.blit(graj, (330, height/2-50))
            menupng = pygame.image.load("img/menu.png")
            self.surface.blit(menupng, (330, height/2+10))
            wyjdz = pygame.image.load("img/quit.png")
            self.surface.blit(wyjdz, (330, height/2+70))

            pygame.display.update()
    def pauza(self, p):
        global PAUZA
        if(p==0):
            PAUZA=0
        elif(p==1):
            PAUZA=1

    def get_pauza(self):
        return PAUZA