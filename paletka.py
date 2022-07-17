import pygame
from rysowanie import Rysuj
class Paletka(Rysuj):
    """
    Rakietka, porusza się w osi X z ograniczeniem prędkości.
    """

    def __init__(self,  width, height, x, y, numer, max_speed=100):
        super(Paletka, self).__init__( width, height, x, y, numer)
        self.max_speed = max_speed
        self.max_speed_ai = max_speed / 10
        #self.surface.fill(color)
        my_image = pygame.image.load("img/paletki/" + str(numer) + ".png")
        self.surface.blit(my_image,(0,0))

    def move(self, x):
        """
        Przesuwa rakietkę w wyznaczone miejsce.
        """
        delta = x - self.rect.x
        if abs(delta) > self.max_speed:
            delta = self.max_speed if delta > 0 else -self.max_speed
        self.rect.x += delta

    def move_ai(self, x):
        """
        Przesuwa rakietke AI (zwolniona predkosc)
        """
        delta = x - self.rect.x
        if abs(delta) > self.max_speed_ai:
            delta = self.max_speed_ai if delta > 0 else -self.max_speed_ai
        self.rect.x += delta