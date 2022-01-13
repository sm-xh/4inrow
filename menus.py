import sys
import time

import numpy as np
import pygame
from gameLogic import *
from constans import *


class userInterface:
    """Klasa bazowa definujaca interfejs uzytkownika"""

    def __init__(self):
        """konstruktor inicjalizujący ustawienia gry"""
        self.game = Game()
        self.run = True
        self.click = False

        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Connect Four")
        pygame.init()
        pygame.font.init()
        # kolory
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.green = (0, 100, 30)
        self.white = (255, 255, 255)
        # kofiguracja czcionek
        self.bigFont = pygame.font.SysFont(None, 80)
        self.mediumFont = pygame.font.SysFont(None, 50)
        self.smallFont = pygame.font.SysFont(None, 20)

    def startScreen(self):
        """funkcja definiująca ekran startowy"""
        skip = False
        self.gameDisplay.fill((88, 111, 200))

        button_start = pygame.Rect(200, 150, 400, 80)
        button_help = pygame.Rect(200, 300, 400, 80)
        button_quit = pygame.Rect(200, 450, 400, 80)

        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_start)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_help)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_quit)

        play = self.bigFont.render("Start Game", True, (0, 0, 0))
        rules = self.bigFont.render("Rules", True, (0, 0, 0))
        quit = self.bigFont.render("Quit", True, (0, 0, 0))

        self.gameDisplay.blit(play, (250, 160))
        self.gameDisplay.blit(rules, (320, 315))
        self.gameDisplay.blit(quit, (330, 460))

        while not skip:
            self.clock.tick(30)
            # lokalizacja kursora myszki
            mx, my = pygame.mouse.get_pos()

            if button_start.collidepoint((mx, my)):
                if self.click == True:
                    self.game.twoPlayer = True
                    self.playgame()
            if button_help.collidepoint(((mx, my))):
                if self.click == True:
                    self.about()
            if button_quit.collidepoint((mx, my)):
                if self.click == True:
                    pygame.quit()
                    sys.exit()

            self.click = False
            # detekcja wyjścia z gry
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                pygame.display.update()

    def about(self):

        instructions_txt = 'Gra rozgrywana jest na pionowym, pustym, drewnianym urządzeniu, w którym gracze na \n \
        przemian upuszczają swoje kafelki na wierzch. Pole gry składa się z 7 pionowych kolumn i 6 poziomych linii. \n \
        Obaj gracze mają po 21 identycznych kolorowych płytek. Kiedy gracz upuszcza element do kolumny, zajmuje \n \
        najniższą dostępną przestrzeń w kolumnie. Każdy gracz jest reprezentowany przez jego kolor \n \
        (na przykład brązowy dla pierwszego gracza i żółty dla drugiego). \n \
        Jest odtwarzany naprzemiennie. Celem gry jest posiadanie czterech kawałków koloru z rzędu. \n \
        Ten wiersz może być pionowy, poziomy lub ukośny. Możesz to zrobić, umieszczając kamienie jeden \n \
        po drugim w siedmiu możliwych kolumnach. Kamienie spadają na najniższą możliwą wolną przestrzeń \n \
        albo na ziemię, albo na inny kamień.'.split('\n')

        self.gameDisplay.fill((66, 111, 155))

        button_return = pygame.Rect(200, 500, 500, 80)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_return)
        return_to = self.bigFont.render("Powrót do menu", True, (0, 0, 0))
        self.gameDisplay.blit(return_to, (250, 520))

        aboutscreen = []
        for i in range(len(instructions_txt)):
            aboutscreen.append(self.smallFont.render(instructions_txt[i], True, (0, 0, 0)))
            self.gameDisplay.blit(aboutscreen[i], (60, 20 * i+1 + 200))

        skip = False
        while not skip:
            self.clock.tick(30)  # This limits the while loop to a max of 10 times per second.

            mx, my = pygame.mouse.get_pos()
            if button_return.collidepoint((mx, my)):
                if self.click == True:
                    skip = True
                    self.startScreen()
            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                pygame.display.update()

    def playgame(self):
        self.gameDisplay.fill(self.green)

        """petla rysujaca plansze"""
        for row in range(1, ROW_COUNT + 1):
            for column in range(1, COLUMN_COUNT + 1):
                pygame.draw.circle(self.gameDisplay, self.white, (column * 100, row * 100 + 130), 30)

        """petla rysujaca przyciski"""
        coin_buttons = []
        for row in range(1, COLUMN_COUNT + 1):
            coin_buttons.append(pygame.Rect([row * 100 - 25, 100, 50, 50]))
            pygame.draw.rect(self.gameDisplay, (255, 0, 0), coin_buttons[row - 1])
            pygame.draw.rect(self.gameDisplay, (220, 20, 190), [row * 100 - 20, 105, 40, 40])

        reset_button = pygame.Rect([320, 20, 160, 40])
        pygame.draw.rect(self.gameDisplay, (0, 40, 200), reset_button)
        reset_text = self.mediumFont.render('RESET', True, (0, 0, 0))
        self.gameDisplay.blit(reset_text, (340, 24))

        """glowna petla gry"""
        while self.run:
            self.clock.tick(30)
            mx, my = pygame.mouse.get_pos()

            for x in coin_buttons:
                if x.collidepoint(((mx, my))):
                    if self.click:
                        pos = pygame.mouse.get_pos()
                        row, column = self.game.player_move(pos)
                        if (row == -1 or column == -1): continue
                        pygame.draw.circle(self.gameDisplay, self.red if self.game.turn == 1 else self.yellow,
                                           ((column + 1) * 100, (row + 1) * 100 + 130), 30)
                        self.game.isGameOver()      #sprawdzenie czy gra sie nie zakonczyla op kazdym ruchu
            if reset_button.collidepoint((mx, my)):
                if self.click:
                    self.playAgain()

            player1 = self.mediumFont.render('Czerwony', 1, self.red if self.game.turn == 1 else (self.green))
            player2 = self.mediumFont.render('Żółty', 1, self.yellow if self.game.turn == 2 else (self.green))
            self.gameDisplay.blit(player1, (50, 24))
            self.gameDisplay.blit(player2, (650, 24))
            self.click = False
            if not self.game.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.click = True

            else:
                self.endOfGame()
            pygame.display.update()

    def playAgain(self):
        """funkcja resetujaca gre"""
        self.game = Game()
        self.startScreen()

    def endOfGame(self):
        """funkcja implementujaca menu koncowe gry"""
        self.gameDisplay.fill((0, 0, 0))

        #ponizsze instrukcje implementuja menu koncowe
        if self.game.winner == 'REMIS':
            congrats = self.mediumFont.render('REMIS!', 1, (0, 0, 0))
        else:
            congrats = self.mediumFont.render(self.game.getTurn() + ' Wygrywa!!!!', True , (0, 0, 0))
        pygame.draw.rect(self.gameDisplay, (200, 0, 0) if self.game.turn == 1 else (255, 255, 0), (0, 0, 800, 52))
        self.gameDisplay.blit(congrats, (200, 15))
        instruction = self.mediumFont.render("Kliknij Reset lub Wyjdz z gry!", True, (255, 255, 255))

        pygame.draw.rect(self.gameDisplay,(102, 204, 80),(100,200,600,400))

        self.gameDisplay.blit(instruction,(170,300))

        button_play = pygame.Rect(200, 400, 400, 80)
        button_quit = pygame.Rect(200, 500, 400, 80)

        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_play)
        pygame.draw.rect(self.gameDisplay, (255, 0, 0), button_quit)

        play_again = self.mediumFont.render("Zagraj ponownie", True, (0, 0, 0))
        quit_game = self.mediumFont.render("Wyjscie", True, (0, 0, 0))

        self.gameDisplay.blit(play_again, (280, 420))
        self.gameDisplay.blit(quit_game, (330, 520))


        #pętla oczekująca na wybór gracza po rozgrywce
        skip = False
        while not skip:
            self.clock.tick(30)  # This limits the while loop to a max of 10 times per second.
            mx, my = pygame.mouse.get_pos()
            if button_play.collidepoint((mx, my)):
                if self.click == True:
                    skip = True
                    self.playAgain()
            if button_quit.collidepoint((mx, my)):
                if self.click == True:
                    pygame.quit()
                    sys.exit()

            self.click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                pygame.display.update()
