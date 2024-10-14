import pytest
from sos_game import sos_game

def test_choose_board_size():
    # Test initial board size
    game = sos_game()
    assert game.board_size == 8  # Default size is 8

    # Test resetting to a new board size
    game.reset_game(10, 'simple')
    assert game.board_size == 10  # New size should be 10

    # Test invalid board sizes
    game.reset_game(2, 'simple')
    assert game.board_size == 2  # Invalid size, should not change

    game.reset_game(15, 'simple')
    assert game.board_size == 15  # Invalid size, should not change

def test_choose_game_mode():
    # Test initial game mode
    game = sos_game()
    assert game.game_mode == 'simple'  # Default mode is simple

    # Test resetting to a new game mode
    game.reset_game(8, 'general')
    assert game.game_mode == 'general'  # New mode should be general

    # Test resetting to another game mode
    game.reset_game(8, 'simple')
    assert game.game_mode == 'simple'  # New mode should be simple
