import pygame

import pileczka
from pileczka import Pilka

pauza =0

class Punkty(object):
    """
    Sędzia gry
    """

    def __init__(self, board, ball, *args):
        self.ball = ball
        self.board = board
        self.rackets = args
        self.score = [0, 0]
        self.pauza = pauza

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)

    def paused(self):

        while(self.pauza==0):
            for event in pygame.event.get():
               if event.type == pygame.locals.MOUSEBUTTONDOWN:
                   self.pauza = 1
        pygame.display.update()

    def update_score(self, board_height):
        """
        Jeśli trzeba przydziela punkty i ustawia piłeczkę w początkowym położeniu.
        """
        if self.ball.rect.y < 0:
            self.score[0] += 1
            print('Punkt dla ciebie')
            self.pauza = 0
            self.paused()
            self.ball.reset()
        elif self.ball.rect.y > board_height - self.ball.rect[3]:
            self.score[1] += 1
            print('Punkt dla przeciwnika')
            self.pauza = 0
            self.paused()
            self.ball.reset()

    def draw_text(self, surface,  text, x, y):
        """
        Rysuje wskazany tekst we wskazanym miejscu
        """
        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):
        """
        Aktualizuje i rysuje wyniki
        """
        height = self.board.surface.get_height()
        self.update_score(height)

        width = self.board.surface.get_width()
        self.draw_text(surface, "{}".format(self.score[1]), width/2, height * 0.3)
        self.draw_text(surface, "{}".format(self.score[0]), width/2, height * 0.7)
