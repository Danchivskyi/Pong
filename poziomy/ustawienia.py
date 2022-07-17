from pileczka import Pilka
from paletka import Paletka
from przeszkody import Przeszkody

width=800
height=400
KOLOR_PALETKI = 1
KOLOR_PILKI = 1

class ustawienia(object):
    def wczytaj_ust(self, widthx, heightx):
        global KOLOR_PALETKI
        global KOLOR_PILKI
        global width
        global height
        width = widthx
        height = heightx
        filename = str('ustawienia.txt')
        f = open(filename, 'r')
        for line in f:
            if line.startswith("kol_paletki:"):
                KOLOR_PALETKI = int(line[12])
            if line.startswith("kol_pilki:"):
                KOLOR_PILKI = int(line[10])
        print(KOLOR_PILKI)
        print(KOLOR_PALETKI)
        f.close()

    def __init__(self):
        self.wczytaj_ust()

    def player1(self):
        if (KOLOR_PALETKI == 1):
            return Paletka( width=80, height=20, x=width / 2 - 40, y=height - 40, numer=1)
        if (KOLOR_PALETKI == 2):
            return Paletka(width=80, height=20, x=width / 2 - 40, y=height - 40, numer=2)
        else:
            return Paletka(width=80, height=20, x=width / 2 - 40, y=height - 40, numer=3)

    def pilka(self):
        if (KOLOR_PILKI == 1):
            return Pilka(20, 20, width / 2, height / 2, numer=1)
        if (KOLOR_PILKI == 2):
            return Pilka(20, 20, width / 2, height / 2, numer=2)
        else:
            return Pilka(20, 20, width / 2, height / 2, numer=3)

    def player2(self):
        return Paletka(width=80, height=20, x=width / 2 - 40, y=20, numer=1)

    def przeszkody(self):
        return Przeszkody(800,20,20,20)