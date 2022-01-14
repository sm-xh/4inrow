from gameLogic import *

def test_init_move():
    test_game = Game()

    test_game.player_move((100,0))
    test_game.changeTurn()
    test_game.player_move((200,0))
    test_game.changeTurn()
    test_game.player_move((300,0))
    test_game.changeTurn()
    test_game.player_move((400,0))

    assert list(test_game.board[-1]).count(0) == 3

def test_winning_horizontally():
    test_game = Game()
    column=(200,0)
    test_game.player_move(column)
    column=(300,0)
    test_game.player_move(column)
    column=(400,0)
    test_game.player_move(column)
    column=(500,0)
    test_game.player_move(column)
    test_game.isGameOver()
    assert test_game.winner == "CZERWONY"

def test_winning_vertically():
    test_game = Game()
    test_game.changeTurn()
    column=(200,0)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.player_move(column)
    test_game.isGameOver()
    assert test_game.winner == "ŻÓŁTY"

def test_winning_plus4_in_row():
    test_game = Game()

    #ustawianie kolejnych zetonow na sobie
    test_game.player_move((100,0))
    test_game.changeTurn()
    test_game.player_move((100,0))

    test_game.changeTurn()
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))

    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))
    
    test_game.changeTurn()
    test_game.player_move((500, 0))
    test_game.changeTurn()
    test_game.player_move((500, 0))

    test_game.changeTurn()
    test_game.player_move((600, 0))
    test_game.changeTurn()
    test_game.player_move((600, 0))

    test_game.changeTurn()
    test_game.player_move((700, 0))
    test_game.changeTurn()
    test_game.player_move((700, 0))

    test_game.changeTurn()
    test_game.player_move((400, 0))
    test_game.isGameOver()
    assert test_game.winner == "CZERWONY"

def test_winning_cross():
    test_game = Game()
    #1sza kolumna
    test_game.player_move((100,0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))
    test_game.changeTurn()
    test_game.player_move((100, 0))

    #2ga kolumna
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))
    test_game.changeTurn()
    test_game.player_move((200, 0))

    test_game.changeTurn()
    test_game.player_move((300, 0))
    test_game.changeTurn()
    test_game.player_move((300, 0))

    test_game.player_move((400, 0))
    test_game.isGameOver()
    assert test_game.winner == "ŻÓŁTY"

test_winning_cross()