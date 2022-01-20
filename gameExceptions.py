from tkinter import *
from tkinter import messagebox



class WrongBoardSizeException(Exception):
    """wyjątek zgłaszany, gdy obszar gry jest inny niż 6x7"""
    def __init__(self):
        self.message="Rozgrywka nie może być rozpoczęta!!! Rozmiar pola do gry jest inny niż 6x7."
        Tk().wm_withdraw()
        messagebox.showinfo('BŁĄD', self.message)

class ColumnFullException(Exception):
    """wyjątek zgłaszany, gdy kolumna została już zapełniona"""
    def __init__(self):
        self.message="Kolumna jest zapełniona, wybierz inną.."
        Tk().wm_withdraw()
        messagebox.showinfo('Uwaga!', self.message)
