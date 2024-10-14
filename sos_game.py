class sos_game:
    def __init__(self, board_size=8, game_mode='simple'):
        self.board_size = board_size
        self.current_player = 'blue'
        self.game_mode = game_mode
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_letter(self, row, col, letter):
        if self.board[row][col] == '':
            self.board[row][col] = letter
            self.current_player = 'red' if self.current_player == 'blue' else 'blue'
            return True
        return False

    def reset_game(self, board_size, game_mode):
        self.board_size = board_size
        self.game_mode = game_mode
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'blue'
