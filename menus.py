import sys
import pygame
from gameLogic import *
from constans import *
from gameExceptions import WrongBoardSizeException


class userInterface:
    """Klasa bazowa definujaca interfejs uzytkownika"""

    def __init__(self):
        """konstruktor inicjalizujący ustawienia gry"""
        # zmienne gry
        self._game = Game()
        self._run = True
        self._click = False
        # ustawienia pygame
        self._gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Connect Four")
        pygame.init()
        pygame.font.init()
        self._clock = pygame.time.Clock()
        # kolory
        self._red = (255, 0, 0)
        self._yellow = (255, 212, 0)
        self._black = (46, 41, 78)
        self._green = (0, 100, 30)
        self._gray = (234, 222, 218)
        self._white = (255, 255, 255)
        self._blue = (0,0,255)
        self._cadetblue = (95,158,160)
        # kofiguracja czcionek
        self._bigFont = pygame.font.SysFont("Consolas", 60)
        self._mediumFont = pygame.font.SysFont("Consolas", 40)
        self._smallFont = pygame.font.SysFont("Consolas", 20)

    def startScreen(self):
        """funkcja definiująca ekran startowy"""
        skip = False  # zmienna do zapetlania menu
        self._gameDisplay.fill((self._cadetblue))

        # przyciski
        button_start = pygame.Rect(200, 150, 400, 80)
        button_help = pygame.Rect(200, 300, 400, 80)
        button_quit = pygame.Rect(200, 650, 400, 80)

        pygame.draw.rect(self._gameDisplay, (255, 0, 0), button_start, border_bottom_right_radius=10)
        pygame.draw.rect(self._gameDisplay, (255, 0, 0), button_help, border_bottom_right_radius=10)
        pygame.draw.rect(self._gameDisplay, (255, 0, 0), button_quit, border_bottom_right_radius=10)

        play = self._bigFont.render("Rozpocznij", True, (0, 0, 0))
        rules = self._bigFont.render("Zasady", True, (0, 0, 0))
        quit = self._bigFont.render("Wyjscie", True, (0, 0, 0))

        self._gameDisplay.blit(play, (230, 160))
        self._gameDisplay.blit(rules, (310, 315))
        self._gameDisplay.blit(quit, (310, 660))

        # pętla menu głównego
        while not skip:
            self._clock.tick(30)
            # lokalizacja kursora myszki
            mx, my = pygame.mouse.get_pos()
            # detekcja klikniecia w przycisk
            if button_start.collidepoint((mx, my)):
                if self._click:
                    self._game.twoPlayer = True
                    self.playgame()
                    skip = True
            if button_help.collidepoint(((mx, my))):
                if self._click:
                    self.about()
                    skip = True
            if button_quit.collidepoint((mx, my)):
                if self._click:
                    pygame.quit()
                    sys.exit()

            self._click = False

            # obsluga eventow
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self._click = True
                pygame.display.update()

    def about(self):
        self._gameDisplay.fill((66, 111, 155))
        instructions_txt = '\n \
        Gra rozgrywana jest na pionowym, pustym, drewnianym urządzeniu, \n \
        w którym gracze na przemian upuszczają swoje kafelki na wierzch. \n \
        Pole gry składa się z 7 pionowych kolumn i 6 poziomych linii. \n \
        Obaj gracze mają po 21 identycznych kolorowych płytek. \n \
        Kiedy gracz upuszcza element do kolumny, zajmuje najniższą \n \
        dostępną przestrzeń w kolumnie. \n \
        Każdy gracz jest reprezentowany przez jego kolor \n \
        (na przykład brązowy dla pierwszego gracza i żółty dla drugiego). \n \
        Jest odtwarzany naprzemiennie.'.split('\n')

        aboutscreen = []
        for i in range(len(instructions_txt)):
            aboutscreen.append(self._smallFont.render(instructions_txt[i], True, self._white))
            self._gameDisplay.blit(aboutscreen[i], (-40 , 20 * i + 1 + 200))

        # przycisk powrot do menu
        button_return = pygame.Rect(200, 560, 500, 80)
        pygame.draw.rect(self._gameDisplay, (255, 0, 0), button_return, border_bottom_right_radius=10)
        return_to = self._bigFont.render("Powrót do menu", True, (0, 0, 0))
        self._gameDisplay.blit(return_to, (220, 580))

        skip = False

        # petla glowna menu z instrukcjami
        while not skip:
            self._clock.tick(30)

            mx, my = pygame.mouse.get_pos()  # pozycja myszki
            # detekcja klikniecia w przycisk
            if button_return.collidepoint((mx, my)):
                if self._click:
                    skip = True
                    self.startScreen()

            self._click = False
            # obsluga eventow
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self._click = True
                pygame.display.update()

    def playgame(self):
        """funkcja obslugujaca faktyczna rozgrywke"""
        self._gameDisplay.fill(self._green)

        # petla rysujaca plansze
        for row in range(1, ROW_COUNT + 1):
            for column in range(1, COLUMN_COUNT + 1):
                pygame.draw.circle(self._gameDisplay, self._black, (column * 100, row * 100 + 130), 33)
                pygame.draw.circle(self._gameDisplay, self._white, (column * 100, row * 100 + 130), 30)

        # obsługa wyjątku związanego z złym rozmiarem okna gry
        if ROW_COUNT != 6 or COLUMN_COUNT != 7:
            raise WrongBoardSizeException

        # petla rysujaca przyciski
        coin_buttons = []
        for row in range(1, COLUMN_COUNT + 1):
            coin_buttons.append(pygame.Rect([row * 100 - 25, 100, 50, 50]))
            pygame.draw.rect(self._gameDisplay, self._black, coin_buttons[row - 1])
            pygame.draw.rect(self._gameDisplay, self._gray, [row * 100 - 20, 105, 40, 40])

        # rysuj przycisk reset
        reset_button = pygame.Rect([320, 20, 160, 40])
        pygame.draw.rect(self._gameDisplay, (0, 40, 200), reset_button, border_bottom_right_radius=10)
        reset_text = self._mediumFont.render('RESET', True, (0, 0, 0))
        self._gameDisplay.blit(reset_text, (340, 24))

        # pętla główna gry
        while self._run:
            self._clock.tick(30)
            mx, my = pygame.mouse.get_pos()  # lokalizacja myszki

            # detekcja klikniecia w przycisk do wrzucania monet
            for x in coin_buttons:
                if x.collidepoint(((mx, my))):
                    if self._click:
                        pos = pygame.mouse.get_pos()
                        row, column = self._game.player_move(position=pos)
                        if row == -1 or column == -1: continue
                        pygame.draw.circle(self._gameDisplay, self._red if self._game._turn == 1 else self._yellow,
                                           ((column + 1) * 100, (row + 1) * 100 + 130), 30)
                        self._game.isGameOver()  # sprawdzenie czy gra sie nie zakonczyla po wykonaniu ruchu przez gracza

            # obsluga przycisku do resetu gry
            if reset_button.collidepoint((mx, my)):
                if self._click:
                    self.playAgain()

            # wypisywanie kolejno informacji kogo tura
            player1 = self._mediumFont.render('Czerwony', 1, self._red if self._game._turn == 1 else (self._green))
            player2 = self._mediumFont.render('Żółty', 1, self._yellow if self._game._turn == 2 else (self._green))
            self._gameDisplay.blit(player1, (50, 24))
            self._gameDisplay.blit(player2, (650, 24))

            self._click = False
            # obsluga eventow
            if not self._game._game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self._click = True
            else:
                self.endOfGame()
            pygame.display.update()

    def playAgain(self):
        """funkcja resetujaca gre"""
        self._game = Game()
        self.startScreen()

    def endOfGame(self):
        """funkcja implementujaca menu koncowe gry"""
        pygame.draw.rect(self._gameDisplay, self._gray, (0, 0, 800, 190))
        # wypisz kolor zwyciezcy gry
        if self._game._winner == 'REMIS':
            congrats = self._mediumFont.render('REMIS!', 1, (0, 0, 0))
        else:
            congrats = self._mediumFont.render(self._game.getTurn() + ' WYGRYWA!!!!', True, (0, 0, 0))
        pygame.draw.rect(self._gameDisplay, (200, 0, 0) if self._game._turn == 1 else (255, 255, 0), (0, 0, 800, 52))
        self._gameDisplay.blit(congrats, (200, 7))

        button_play = pygame.Rect(40, 85, 440, 60)
        button_quit = pygame.Rect(550, 85, 220, 60)

        pygame.draw.rect(self._gameDisplay, self._red, button_play, border_bottom_right_radius=10)
        pygame.draw.rect(self._gameDisplay, self._blue, button_quit, border_bottom_right_radius=10)

        play_again = self._mediumFont.render("Zagraj ponownie", True, (0, 0, 0))
        quit_game = self._mediumFont.render("Wyjscie", True, (255, 255, 255))

        self._gameDisplay.blit(play_again, (60, 95))
        self._gameDisplay.blit(quit_game, (570, 95))

        # pętla oczekująca na wybór gracza po rozgrywce
        skip = False
        while not skip:
            self._clock.tick(30)
            mx, my = pygame.mouse.get_pos()  # lokalizacja myszki
            # obsluga klikniecia w przycisk
            if button_play.collidepoint((mx, my)):
                if self._click == True:
                    skip = True
                    self.playAgain()
            if button_quit.collidepoint((mx, my)):
                if self._click == True:
                    skip = True
                    pygame.quit()
                    sys.exit()

            self._click = False
            # obsluga eventow
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self._click = True
                pygame.display.update()
