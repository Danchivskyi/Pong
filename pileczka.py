import pygame

import przeszkody
from rysowanie import Rysuj
#from paletka import Paletka

width = 800
height = 400

class Pilka(Rysuj):
    """
    Piłeczka, sama kontroluje swoją prędkość i kierunek poruszania się.
    """
    def __init__(self, width, height, x, y, numer, x_speed=3, y_speed=3):
        super(Pilka, self).__init__(width, height, x, y, numer)

        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
        my_image = pygame.image.load("img/pilki/" + str(numer) + ".png")
        self.surface.blit(my_image,(0,0))
        #self.rectx = self.surface.get_rect()
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y


    def bounce_y(self, predkosc):
        """
        Odwraca wektor prędkości w osi Y
        """
        self.y_speed *= -1 * predkosc

        #print(self.y_speed)
       # print(self.rect.x)


    def bounce_x(self, predkosc):
        """
        Odwraca wektor prędkości w osi X
        """
        self.x_speed *= -1 * predkosc



    def reset(self):
        """
        Ustawia piłeczkę w położeniu początkowym i odwraca wektor prędkości w osi Y
        """
        #self.rect.move(self.start_x, self.start_y)
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.x_speed = 3
        self.y_speed = 3

        #@self.bounce_y(-1)
    def move_przeszkody(self, board, *args):
        """
        Przesuwa piłeczkę o wektor prędkości
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0 or self.rect.x > board.surface.get_width() - self.width:
            self.bounce_x(1)

        if self.rect.y < 0 or self.rect.y > board.surface.get_height() - self.height:
            self.bounce_y(1)

        for racket in args:
            if self.rect.colliderect(racket.rect):
                paletka_s = racket.rect[0]
                paletka_k = racket.rect[0] + 80
                paletka_ktora = racket.rect[1]
                roznica = paletka_k - self.rect.x
                print(roznica)

    def move(self, board, *args):
        """
        Przesuwa piłeczkę o wektor prędkości
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0 or self.rect.x > board.surface.get_width() - self.width:
            self.bounce_x(1)

        if self.rect.y < 0 or self.rect.y > board.surface.get_height() - self.height:
            self.bounce_y(1)

       # for racket in args:
       #     print(racket.__repr__()[:10])




#"""
        for racket in args:
            if self.rect.colliderect(racket.rect):
                paletka_s = racket.rect[0]
                paletka_k = racket.rect[0] + 80
                paletka_ktora = racket.rect[1]
                #print(self.rect)
                #print(self.rect.x)
                roznica = paletka_k - self.rect.x
                #print(racket.rect[2])


                if(roznica > 0 and roznica < 34): #prawa strona
                    if(paletka_ktora == 20): #gorna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_y(1)
                            self.bounce_x(-1.2)
                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_x(1.2)
                            self.bounce_y(-1)
                    if (paletka_ktora == 360):  #dolna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_x(1.2)
                            self.bounce_y(-1)
                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_y(1)
                            self.bounce_x(-1.2)
                if(roznica >= 36 and roznica < 54): #srodek
                    if(paletka_ktora == 20): #gorna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_y(0.7)
                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_y(0.7)
                    if (paletka_ktora == 360):  #dolna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_y(0.7)
                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_y(0.7)
                    #self.bounce_x()
                if(roznica >= 55 and roznica < 100): #lefa strona paletki
                    if(paletka_ktora == 20): #gorna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_x(-1.2)
                            self.bounce_y(1)

                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_y(-1.2)
                            self.bounce_x(1)
                    if (paletka_ktora == 360):  #dolna
                        if(self.x_speed < 0): # w lewa strone leci pilka
                            self.bounce_y(1)
                            self.bounce_x(-1.2)
                        if(self.x_speed > 0): # prawa strone leci pilka
                            self.bounce_x(1)
                            self.bounce_y(-1.2)
