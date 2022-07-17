width = 800
height = 400

class Ai(object):
    """
    Przeciwnik, steruje swoją rakietką na podstawie obserwacji piłeczki.
    """
    def __init__(self, racket, ball):
        self.ball = ball
        self.racket = racket

    def move(self):
        x = self.ball.rect.centerx
        if(x<800-80):
            #self.racket.move(x)
            self.racket.move_ai(x)