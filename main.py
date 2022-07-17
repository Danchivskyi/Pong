import time

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import sys
from random import randrange
from typing import Tuple, Any, Optional, List
from rysowanie import Rysuj
import kontroler

KOLOR_PILKI=1
KOLOR_PALETKI=1
width=800
height=400
ABOUT = ['Witamy witamy. Gra Pong napisana',
         'przez studentów 3EF-DI/TT',
         'Michał Cempa oraz Oleh Danchivskyi']
FPS = 60
WINDOW_SIZE = (width, height + 80)
def play_function(poziom) -> None:
    game = kontroler.Pong(width, height, poziom)
    game.run()

def main_background() -> None:
    """Funkcja używana przez menu, rysowanie w tle, gdy menu jest aktywne."""
    global surface
    surface.fill((53, 82, 179))

def zmien_kolor_paletki(value: Tuple[Any, int], kolor: int, obj) -> None:
    global KOLOR_PALETKI
    KOLOR_PALETKI = kolor
    paletka_store = obj
    paletka_store.remove_widget('paletka')
    paletka_store.add.image("img/paletki/" + str(KOLOR_PALETKI) + ".png", angle=0,image_id="paletka", scale=(1, 1), scale_smooth=True,selectable=False, margin=(5,10))

    filename = str('ustawienia.txt')
    text = str(kolor)
    with open(filename, "r") as file:
        lines = file.readlines()
    lines[0] = "kol_paletki:" + str(text) + "\n"

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)

    #f.write(f"kol_paletki:{text}")
    file.close()

def zmien_kolor_pilki(value: Tuple[Any, int], kolor: int, obj) -> None:
    global KOLOR_PILKI
    KOLOR_PILKI = kolor
    pilka_store = obj
    pilka_store.remove_widget('pilka')
    pilka_store.add.image("img/pilki/" + str(KOLOR_PILKI) + ".png", angle=0,image_id="pilka", scale=(1, 1), scale_smooth=True,selectable=False, margin=(5,10))

    #pilka_store.
    filename = str('ustawienia.txt')
    text = str(kolor)
    with open(filename, "r") as file:
        lines = file.readlines()

    lines[1] = "kol_pilki:" + str(text) + "\n"

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)


    #f.write(f"kol_paletki:{text}")
    file.close()

def wczytaj_ust():
    global KOLOR_PALETKI
    global KOLOR_PILKI
    global width
    global height
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

def main(test: bool = False) -> None:
    """Program główny."""

    # -------------------------------------------------------------------------
    # Zmienne globalne
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Tworzenie okienka
    # -------------------------------------------------------------------------
    surface = create_example_window('Gra "Pong"', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Tworzenie menu: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Menu',
        width=WINDOW_SIZE[0] * 0.75
    )

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_wybierz = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_theme,
        title='Poziomy',
        width=WINDOW_SIZE[0] * 0.7
    )
    play_wybierz.add.button(f'Poziom 1', play_function,1)
    play_wybierz.add.button(f'Poziom 2', play_function,2)

    play_wybierz.add.button('Wróc do menu', pygame_menu.events.RESET)

    play_menu.add.button('Start',
                         play_function,1)
    play_menu.add.button('Wybierz poziom', play_wybierz)
    play_menu.add.button('Wróc do menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Tworzenie menu:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.widget_margin = (0, 0)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=about_theme,
        title='O nas',
        width=WINDOW_SIZE[0] * 0.6
    )

    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Wróc do menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Tworzenie menu: Store (będą będzie kupić paletkę lub piłke)
    # -------------------------------------------------------------------------
    store_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Sklep',
        width=WINDOW_SIZE[0] * 0.75
    )

    submenu_themes = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_themes.widget_font_size = 15
    pilka_store = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_themes,
        title='Piłeczki',
        width=WINDOW_SIZE[0] * 0.7
    )

    paletka_store = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_themes,
        title='Paletki',
        width=WINDOW_SIZE[0] * 0.7


    )
   # print(pygame_menu.Menu.get_(paletka_store))
    #he.add.image("img/paletki/" + str(KOLOR_PALETKI) + ".png", angle=0, scale=(5, 5), scale_smooth=True, margin=(100,20))

    #pilka_store.remove_widget('pilka')
    store_menu.add.button('Piłka', pilka_store)
    pilka_store.add.selector('Wybierz piłeczkę: ',
                           [('1', '1', pilka_store),
                            ('2', '2', pilka_store),
                            ('3', '3', pilka_store)],
                           onchange=zmien_kolor_pilki,
                            margin=(0,15))
    store_menu.add.button('Paletka', paletka_store)
    paletka_store.add.selector('Wybierz paletke: ',
                           [('1', '1', paletka_store),
                            ('2', '2', paletka_store),
                            ('3', '3', paletka_store)],
                           onchange=zmien_kolor_paletki,
                            margin=(0,15))
    # -------------------------------------------------------------------------
    paletka_store.add.image("img/paletki/" + str(KOLOR_PALETKI) + ".png",image_id="paletka", angle=0, scale=(1, 1), scale_smooth=True, margin=(5,100))
    pilka_store.add.image("img/pilki/" + str(KOLOR_PILKI) + ".png", image_id="pilka" ,angle=0, scale=(1, 1), scale_smooth=True, margin=(5,-100))
    # -------------------------------------------------------------------------
    # Tworzenie menu: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=main_theme,
        title='Menu Główne',
        width=WINDOW_SIZE[0] * 0.6
    )

    main_menu.add.button('Graj', play_menu)
    main_menu.add.button('Sklep', store_menu)
    main_menu.add.button('O nas', about_menu)
    main_menu.add.button('Wyjdź', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Pętla główna
    # -------------------------------------------------------------------------
    while True:

        # Zegarek
        clock.tick(FPS)

        # Rysowanie tła
        main_background()

        # Zdarzenie aplikacji
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)
            main_menu.update(events)

        # Odwracanie powierzchni
        pygame.display.flip()

        if test:
            break


if __name__ == '__main__':
    wczytaj_ust()
    main()