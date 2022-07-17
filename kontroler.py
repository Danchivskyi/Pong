import pygame
import pygame.locals
from gra import Plansza
from poziomy.poziom1 import *
from poziomy.poziom2 import *
from punkty import Punkty
from poziomy.ustawienia import  *
from ai import Ai
KOLOR_PALETKI = 3
KOLOR_PILKI = 1
PAUZA=0
class Pong(object):
    """
    laczy elementy w calosc
    """

    def __init__(self, width, height, poziom):
        pygame.init()
        #self.wczytaj_ust()
        self.Plansza = Plansza(width, height)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()
        ustawienia.wczytaj_ust(1, width, height)
        if(poziom==1):

            #poziom1.wczytaj_ust(1, width, height)
            self.player1 = poziom1.player1(1)
            self.Pilka = poziom1.pilka(1)
            self.player2 = poziom1.player2(1)
            self.ai = Ai(self.player2, self.Pilka)
            self.sedzia = Punkty(self.Plansza, self.Pilka, self.player2, self.Pilka)
        if(poziom==2):
            self.przeszkody = poziom2.przeszkody(1)
            self.player1 = poziom2.player1(1)
            self.Pilka = poziom2.pilka(1)
            self.sedzia = Punkty(self.Plansza, self.Pilka, self.player1, self.Pilka)

    def run(self):
        """
        petla programu
        """
        global PAUZA
        while not self.handle_events():

                #self.Pilka.move(self.Plansza, self.player1, self.player2)
                try:
                    if(PAUZA==0 or self.Plansza.get_pauza() == 0 ):
                        if(self.Plansza.get_pauza() == 0):
                            PAUZA=0
                        self.Pilka.move(self.Plansza, self.player1, self.player2)
                    self.Plansza.draw(
                        self.Pilka,
                        self.player1,
                        self.player2,
                        self.sedzia,
                    )
                    self.ai.move()
                except:
                    if(PAUZA==0):
                        if(self.Plansza.get_pauza() == 0):
                            PAUZA=0
                        self.Pilka.move(self.Plansza, self.player1, self.przeszkody)
                    self.Plansza.draw(
                        self.Pilka,
                        self.player1,
                        #self.player2,
                        self.sedzia,
                        self.przeszkody,
                    )
                  #self.ai.move()


                self.fps_clock.tick(30)

    def paused(self):
        global PAUZA
        if(PAUZA==0):
            PAUZA=1
            self.Plansza.pauza(1)

        elif(PAUZA==1):
            PAUZA=0
            self.Plansza.pauza(0)


    def handle_events(self):
        """
        ruchy myszka
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEMOTION:
                # myszka steruje ruchem pierwszego gracza
                x, y = event.pos
                self.player1.move(x)
                if(self.player1.rect.x>width-80):
                    self.player1.move(width-80)
                #print(self.player1.rect.x)

            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("kontroler= " + str(PAUZA))
                    print("gra= " + str(self.Plansza.get_pauza()))
                    self.paused()


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = Pong(800, 400)
    game.run()