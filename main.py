import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

GAME_OVER = False

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board