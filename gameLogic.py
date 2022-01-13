# modul zawierajacy informacje o logice gry
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


class Game:
    def __init__(self):
        """funkcja inicjalizujaca plansze do gry wraz z ustawieniami"""
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT), int)
        self.turn = 1
        self.max_turns = 42
        self.number_of_turns = 0
        self.winner = None
        self.game_over = False

    def resetBoard(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT), int)
    def getTurn(self):
        """funkcja zwracająca informacje o tym, który gracz wykonuje ruch"""
        if self.turn == 1:
            return "CZERWONY"
        elif self.turn == 2:
            return "ŻÓLTY"

    def changeTurn(self):
        """funkcja pozwalająca na zmianę tury"""
        self.number_of_turns = +1
        if self.turn % 2 == 0:
            self.turn = 1
        else:
            self.turn = 2

    def player_move(self, position):
        """funkcja realizująca ruch gracza"""
        column = (position[0]-50)//100   #pozycja jest obliczana na postawie obecnego polozenia myszy
        if column<0:
            column=0
        elif column>6:
            column=6
        for row in range(ROW_COUNT-1,-1,-1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.turn
                self.max_turns =- 1
                return row,column
        return -1,-1

    def isGameOver(self):
        """funkcja weryfikujaca czy rozgrywka nie zostala juz zakonczona"""
        for r in range(3):  # test diagonally ()
            for c in range(4):
                if self.board[r][c] == self.turn and self.board[r][c] == self.board[r + 1][c + 1] and self.board[r + 1][c + 1] == self.board[r + 2][c + 2] and self.board[r + 2][c + 2] == self.board[r + 3][c + 3] :
                    self.game_over = True
                    self.winner = self.getTurn()

        if not self.game_over :
            for r in range(5,2,-1):  # test diagonally (ters birim matris)
                for c in range(4):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r - 1][c + 1] and self.board[r - 1][c + 1] == self.board[r - 2][c + 2] and self.board[r - 2][c + 2] == self.board[r - 3][c + 3]:
                        self.game_over = True
                        self.winner = self.getTurn()

        if not self.game_over : # test horizontally
            for r in range(6):
                for c in range(4):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r][c + 1] and self.board[r][c + 1] == self.board[r][c + 2] and self.board[r][c + 2] == self.board[r][c + 3]:
                        self.game_over = True
                        self.winner = self.getTurn()
        if not self.game_over :
            for r in range(3):  # test vertically
                for c in range(7):
                    if self.board[r][c] == self.turn and self.board[r][c] == self.board[r + 1][c] and self.board[r + 1][c] == self.board[r + 2][c] and self.board[r + 2][c] == self.board[r + 3][c]:
                        self.game_over = True
                        self.winner = self.getTurn()

        if not self.game_over :
            if  self.max_turns == 0 :
                self.winner = 'Draw'
                self.game_over = True
            else :
                self.changeTurn()


