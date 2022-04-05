from turtle import width
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import sys
from random import randrange
from typing import Tuple, Any, Optional, List

# Constants and global variables
ABOUT = ['Witamy witamy. Gra Pong napisana',
        'przez studentów 3EF-DI/TT',
        'Michał Cempa oraz Oleh Danchivskyi']
DIFFICULTY = ['EASY']
FPS = 60
WINDOW_SIZE = (640, 480)

clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None


def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Zmiana poziomu trudności
    difficulty: Parametr opcjonalny przekazany jako argument do add_sector 
    """
    selected, index = value
    print(f'Wybierz trudność: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty


def random_color() -> Tuple[int, int, int]:
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)



def play_function(difficulty: List, font: 'pygame.font.Font', test: bool = False) -> None:
################################ PALETKA ################################
    PALETKA_SZER = 20  # szerokość
    PALETKA_WYS = 100  # wysokość
    BLUE = (0, 0, 255)  # kolor wypełnienia
    PALETKA_1_POZ = (0, 0)  # początkowa pozycja zapisana w tupli
    
    # utworzenie powierzchni paletki, wypełnienie jej kolorem,
    paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
    paletka1.fill(BLUE)
    # ustawienie prostokąta zawierającego paletkę w początkowej pozycji
    paletka1_prost = paletka1.get_rect()
    paletka1_prost.x = PALETKA_1_POZ[0]
    paletka1_prost.y = PALETKA_1_POZ[1]
    surface.blit(paletka1, paletka1_prost)


    PALETKA_2_POZ = (620, 0)
    paletka2 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
    paletka2.fill(BLUE)
    # ustawienie prostokąta zawierającego paletkę w początkowej pozycji
    paletka2_prost = paletka1.get_rect()
    paletka2_prost.x = PALETKA_2_POZ[0]
    paletka2_prost.y = PALETKA_2_POZ[1]
    surface.blit(paletka2, paletka2_prost)

#########################################################################

################################ PIŁKA ################################
    P_SZER = 20  # szerokość
    P_WYS = 20  # wysokość
    P_PREDKOSC_X = 6  # prędkość pozioma x
    P_PREDKOSC_Y = 6  # prędkość pionowa y
    GREEN = (0, 255, 0)  # kolor piłki
    # utworzenie powierzchni piłki, narysowanie piłki i wypełnienie kolorem
    pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
    pygame.draw.ellipse(pilka, GREEN, [0, 0, P_SZER, P_WYS])
    # ustawienie prostokąta zawierającego piłkę w początkowej pozycji
    pilka_prost = pilka.get_rect()
    pilka_prost.x = WINDOW_SIZE[0] / 2
    pilka_prost.y = WINDOW_SIZE[1] / 2

    FPS = 30 
    fpsClock = pygame.time.Clock()
#########################################################################

    # Definicja zmiennych globalnych
    global main_menu
    global clock

    '''if difficulty == 'EASY':
        #f = font.render('Playing as a baby (easy)', True, (255, 255, 255))
    elif difficulty == 'MEDIUM':
        #f = font.render('Playing as a kid (medium)', True, (255, 255, 255))
    elif difficulty == 'HARD':
        #f = font.render('Playing as a champion (hard)', True, (255, 255, 255))
    else:
        raise ValueError(f'unknown difficulty {difficulty}')'''
        
    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))

    # Rysowanie losowego koloru i tekstu
    bg_color = random_color()

    # Resetowanie i wyłączenie głównego menu
    main_menu.disable()
    main_menu.full_reset()

    frame = 0

    while True:
        clock.tick(60)
        frame += 1

        # Zdarzenia aolikacyjne
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()
                    return


        ############### DLA PALETEK GRACZA ###############
        # przechwytywanie ruchu myszy
            elif e.type == pygame.MOUSEMOTION:
                myszaX, myszaY = e.pos  # współrzędne x, y kursora myszy

                # obliczanie przesunięcie paletki gracza
                przesuniecie = myszaY - (PALETKA_WYS / 2)

                # jeżeli wykraczamy poza okno gry w prawo
                if przesuniecie > WINDOW_SIZE[1] - PALETKA_WYS:
                    przesuniecie = WINDOW_SIZE[1] - PALETKA_WYS
                # jeżeli wykraczamy poza okno gry w lewo
                if przesuniecie < 0:
                    przesuniecie = 0
                # aktualizacja położenia paletki w poziomie
                paletka1_prost.y = przesuniecie
                paletka2_prost.y = przesuniecie

        ####################### DLA PIŁKI ############################
            pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)

            if pilka_prost.right >= WINDOW_SIZE[1]:
                        P_PREDKOSC_X *= -1
            if pilka_prost.left <= 0:
                    P_PREDKOSC_X *= -1

            if pilka_prost.top <= 0:  
                    P_PREDKOSC_Y *= -1  

            if pilka_prost.bottom >= WINDOW_SIZE[1]:  # piłka uciekła dołem
                pilka_prost.x = WINDOW_SIZE[1] / 2  # więc startuję ze środka
                pilka_prost.y = WINDOW_SIZE[1] / 2

            if pilka_prost.colliderect(paletka1_prost):
                P_PREDKOSC_Y *= -1
                pilka_prost.bottom = paletka1_prost.top
        ###################################################

        # Przekazanie zdarzenia do main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        # Kontynuacja gry
        surface.fill(bg_color)
       
        surface.blit(paletka1, paletka1_prost)
        surface.blit(paletka2, paletka2_prost)
        surface.blit(pilka, pilka_prost)
        fpsClock.tick(FPS)

        pygame.display.flip()

        if test and frame == 2:
            break


def main_background() -> None:
    """Funkcja używana przez menu, rysowanie w tle, gdy menu jest aktywne."""
    global surface
    surface.fill((128, 0, 128))


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
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_theme,
        title='Submenu',
        width=WINDOW_SIZE[0] * 0.7
    )
    for i in range(5):
        play_submenu.add.button(f'Back {i}', pygame_menu.events.BACK)
    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add.button('Start', 
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
    """play_menu.add.selector('Wybór trudności',
                           [('1 - Easy', 'EASY'),
                            ('2 - Medium', 'MEDIUM'),
                            ('3 - Hard', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')"""
    play_menu.add.button('Another menu', play_submenu)
    play_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Tworzenie menu:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.widget_margin = (0, 0)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.6,
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0] * 0.6
    )

    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to menu', pygame_menu.events.BACK)


    # -------------------------------------------------------------------------
    # Tworzenie menu: Store (będą będzie kupić paletkę lub piłke)
    # -------------------------------------------------------------------------
    store_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        title='Store',
        width=WINDOW_SIZE[0] * 0.75
    )

    submenu_themes = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_themes.widget_font_size = 15
    play_submenus = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.5,
        theme=submenu_themes,
        title='Submenu',
        width=WINDOW_SIZE[0] * 0.7
    )

    store_menu.add.button('Piłka', play_submenus)
    store_menu.add.button('Paletka', play_submenus)
    # -------------------------------------------------------------------------


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

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('Store', store_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

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

        # Odwracanie powierzchni
        pygame.display.flip()

        if test:
            break

        


if __name__ == '__main__':
    main()