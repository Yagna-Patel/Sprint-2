import pytest
from sos_game import sos_game


def test_letter_placement():
    game = sos_game()
    assert game.place_letter(0, 0, 'S') == True
    assert game.board[0][0] == 'S'
    assert game.current_player == 'red'

def test_invalid_placement():
    game = sos_game()
    game.place_letter(0, 0, 'S')
    assert game.place_letter(0, 0, 'O') == False  # can't place a letter in the same spot