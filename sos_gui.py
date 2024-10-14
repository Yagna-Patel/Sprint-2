# sos_gui.py
import tkinter as tk
from tkinter import ttk
from sos_game import sos_game  # Import the game logic
from tkinter import messagebox

class sos_gui:
    def __init__(self, master):
        self.master = master
        self.game = sos_game()  # Initialize the game logic
        self.master.title("SOS Game")
        
        self.create_widgets()

    def create_widgets(self):
        # Game options
        options_frame = ttk.Frame(self.master, padding="10")
        options_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        ttk.Label(options_frame, text="SOS").grid(row=0, column=0, sticky="w")
        self.game_mode_var = tk.StringVar(value="simple")
        ttk.Radiobutton(options_frame, text="Simple game", variable=self.game_mode_var, value="simple").grid(row=0, column=1)
        ttk.Radiobutton(options_frame, text="General game", variable=self.game_mode_var, value="general").grid(row=0, column=2)

        ttk.Label(options_frame, text="Board size").grid(row=0, column=3)
        self.board_size_var = tk.StringVar(value="8")
        ttk.Entry(options_frame, textvariable=self.board_size_var, width=5).grid(row=0, column=4)
        ttk.Button(options_frame, text="Enter", command=self.set_board_size).grid(row=0, column=5, padx=5)

        # Player options
        blue_frame = ttk.Frame(self.master, padding="10")
        blue_frame.grid(row=1, column=0, sticky="nw")
        ttk.Label(blue_frame, text="Blue player").grid(row=0, column=0, columnspan=2)
        self.blue_letter_var = tk.StringVar(value="S")
        ttk.Radiobutton(blue_frame, text="S", variable=self.blue_letter_var, value="S").grid(row=1, column=0)
        ttk.Radiobutton(blue_frame, text="O", variable=self.blue_letter_var, value="O").grid(row=1, column=1)

        red_frame = ttk.Frame(self.master, padding="10")
        red_frame.grid(row=1, column=1, sticky="ne")
        ttk.Label(red_frame, text="Red player").grid(row=0, column=0, columnspan=2)
        self.red_letter_var = tk.StringVar(value="S")
        ttk.Radiobutton(red_frame, text="S", variable=self.red_letter_var, value="S").grid(row=1, column=0)
        ttk.Radiobutton(red_frame, text="O", variable=self.red_letter_var, value="O").grid(row=1, column=1)

        # Game board
        self.board_frame = ttk.Frame(self.master, padding="10")
        self.board_frame.grid(row=2, column=0, columnspan=2)
        self.create_board()

        # Current turn
        self.turn_label = ttk.Label(self.master, text="Current turn: blue")
        self.turn_label.grid(row=3, column=0, columnspan=2)

    def create_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        for i in range(self.game.board_size):
            for j in range(self.game.board_size):
                btn = ttk.Button(self.board_frame, text='', width=3,
                                 command=lambda row=i, col=j: self.on_cell_click(row, col))
                btn.grid(row=i, column=j, padx=1, pady=1)

    def set_board_size(self):
        try:
            board_size = int(self.board_size_var.get())
            if 3 <= board_size <= 12:
                self.game.reset_game(board_size, self.game_mode_var.get())
                self.create_board()
                self.update_turn_label()
            else: messagebox.showwarning("Invalid Size", "Board size must be between 3 and 12.") # warning for board size
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for board size.") # this is incase a user enters a non integer character

    def on_cell_click(self, row, col):
        current_letter = self.blue_letter_var.get() if self.game.current_player == 'blue' else self.red_letter_var.get()
        if self.game.place_letter(row, col, current_letter):
            self.update_board()
            self.update_turn_label()

    def update_board(self):
        for i, row in enumerate(self.game.board):
            for j, cell in enumerate(row):
                self.board_frame.grid_slaves(row=i, column=j)[0]['text'] = cell

    def update_turn_label(self):
        self.turn_label['text'] = f"Current turn: {self.game.current_player}"

if __name__ == "__main__":
    root = tk.Tk()
    app = sos_gui(root)
    root.mainloop()