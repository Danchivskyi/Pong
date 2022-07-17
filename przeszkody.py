from rysowanie import Rysuj

class Przeszkody(Rysuj):

    def __init__(self,  width, height, x, y, color=(0, 255, 0)):
        super(Przeszkody, self).__init__( width, height, x, y, color)
        self.surface.fill(color)
