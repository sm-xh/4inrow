import numpy as np
import pygame
from pygame.locals import *
import sys
import math
from gameLogic import *


class user_interface:
    """Klasa bazowa definujaca interfejs uzytkownika"""

    def __init__(self):
        """konstruktor inicjalizujący ustawienia gry"""
        self.game = Game()
        self.run = True
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.clock = pygame.time.Clock()
        self.gameDisplay = pygame.display.set_mode(1280, 720)
        pygame.display.set_caption("Connect Four")
        pygame.init()
        pygame.font.init()
        # kofiguracja czcionek
        self.bigFont = pygame.font.SysFont(None, 40)
        # self.mediumFont = pygame.font.SysFont(None, 30)
        # self.smallFont = pygame.font.SysFont(None,15)

    def startScreen(self):
        """funkcja definiująca ekran startowy"""
        skip = False
        self.gameDisplay.fill(0, 0, 0)
        play = self.bigFont.render("Start Game", True, (0, 0, 0))
        rules = self.bigFont.render("Rules", True, (0, 0, 0))
        quit = self.bigFont.render("Quit", True, (0, 0, 0))

        self.gameDisplay.blit(play,(300,250))
        self.gameDisplay.blit(rules, (300, 350))
        self.gameDisplay.blit(quit, (300, 450))

        while not skip:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    skip=True
                    self.run=False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0] > 290 and pos[0] < 530) and (pos[1] > 246 and pos[1] < 300)):
                        skip = True
                        self.selectEnemy()
                    elif ((pos[0] > 298 and pos[0] < 400) and (pos[1] > 310 and pos[1] < 340)):
                        skip = True
                        self.about()
                    elif ((pos[0] > 298 and pos[0] < 365) and (pos[1] > 360 and pos[1] < 380)):
                        skip = True
                        self.run = False
                pygame.display.update()

