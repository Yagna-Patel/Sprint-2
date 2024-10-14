class sos_game: # lots of changes and addtions will be made as this is game logic.
    def __init__(self, board_size=8, game_mode='simple'): # we start with a simple 8x8 grid game.
        self.board_size = board_size
        self.current_player = 'blue' # starting player is always blue.
        self.game_mode = game_mode
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)] # creating the empty board with entered size.

    def place_letter(self, row, col, letter): # function plceas a letter (S or O) on the board at row and column.
        if self.board[row][col] == '':
            self.board[row][col] = letter
            self.current_player = 'red' if self.current_player == 'blue' else 'blue' # helps switch current player after cell placement.
            return True # basically being able to place S or O if cell is empty.
        return False # this acts as a blocking method for overwriting already occupied cells.

    def reset_game(self, board_size, game_mode): # function resents the game with a new board cleaning everything.
        self.board_size = board_size
        self.game_mode = game_mode
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)] # creating the new board.
        self.current_player = 'blue' # blue is always starting player. Need to change this depending on the game outcome. 
