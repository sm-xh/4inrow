"""MODUL IMPLEMENTUJE LOGIKE GRY"""
import numpy as np
from constans import *

class Game:
    """Klasa definiuje logike wlasciwa gry za pomoca funkcji"""
    def __init__(self):
        """Konstruktor planszy do gry wraz z ustawieniami"""
        self._board = np.zeros((ROW_COUNT, COLUMN_COUNT), int)
        self._turn = 1
        self._max_turns = 42
        self._number_of_turns = 0
        self._winner = None
        self._game_over = False

    def resetBoard(self):
        """funkcja do resetowania planszy gry"""
        self._board = np.zeros((ROW_COUNT, COLUMN_COUNT), int)

    def getTurn(self):
        """funkcja zwracająca informacje o tym, który gracz wykonuje ruch"""
        if self._turn == 1:
            return "CZERWONY"
        elif self._turn == 2:
            return "ŻÓŁTY"

    def changeTurn(self):
        """funkcja pozwalająca na zmianę tury"""
        self._number_of_turns = +1
        if self._turn % 2 == 0:
            self._turn = 1
        else:
            self._turn = 2

    def player_move(self, position):
        """funkcja realizująca ruch gracza"""
        column = (position[0]-50)//100   #pozycja jest obliczana na postawie obecnego polozenia myszy
        if column<0:
            column=0
        elif column>6:
            column=6
        for row in range(ROW_COUNT-1,-1,-1):
            if self._board[row][column] == 0:
                self._board[row][column] = self._turn
                self._max_turns = self._max_turns - 1
                return row,column
        return -1,-1

    def isGameOver(self):
        """funkcja weryfikujaca czy rozgrywka nie zostala juz zakonczona"""
        #test w pionie
        for r in range(3):
            for c in range(4):
                if self._board[r][c] == self._turn and self._board[r][c] == self._board[r + 1][c + 1] and self._board[r + 1][c + 1] == self._board[r + 2][c + 2] and self._board[r + 2][c + 2] == self._board[r + 3][c + 3] :
                    self._game_over = True
                    self._winner = self.getTurn()

        #test w poziomie
        if not self._game_over:
            for r in range(6):
                for c in range(4):
                    if self._board[r][c] == self._turn and self._board[r][c] == self._board[r][c + 1] and self._board[r][c + 1] == self._board[r][c + 2] and self._board[r][c + 2] == self._board[r][c + 3]:
                        self._game_over = True
                        self._winner = self.getTurn()

        #test na skos
        if not self._game_over:
            for r in range(3):
                for c in range(7):
                    if self._board[r][c] == self._turn and self._board[r][c] == self._board[r + 1][c] and self._board[r + 1][c] == self._board[r + 2][c] and self._board[r + 2][c] == self._board[r + 3][c]:
                        self._game_over = True
                        self._winner = self.getTurn()

        #sprawdzenie czy nie zaszedl remis, a w przeciwnym razie nastepuje zmiana tury
        if not self._game_over :
            if  self._max_turns == 0:
                self._winner = 'REMIS'
                self._game_over = True
            else :
                self.changeTurn()


