import pytest
from sos_game import sos_game

# used stackoverflow to understand how assert works.
def test_letter_placement(): # test to check that letter is placed correctly in empty cell.
    game = sos_game()
    assert game.place_letter(0, 0, 'S') == True # place S at row 0 and col 0.
    assert game.board[0][0] == 'S' # if S os placed correctly.
    assert game.current_player == 'red' # switch player.

# checking to see if its false when trying to place letter in occupied cell.
def test_invalid_placement(): 
    game = sos_game()
    game.place_letter(0, 0, 'S') # place S at row 0 and col 0 to occupy the cell.
    assert game.place_letter(0, 0, 'O') == False  # if place O in occpied cell it should be false.
