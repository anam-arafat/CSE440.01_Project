import tkinter as tk
from tkinter import font as tkfont
from game import TicTacToe
from ai import AIPlayer

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with AI")

        # Custom font for UI elements
        self.custom_font = tkfont.Font(family="Avenir", size=16, weight="bold")

        # Set window size and center it
        self.window_width = 400
        self.window_height = 500
        self.center_window(self.window_width, self.window_height)

        # Create Tic-Tac-Toe game and AI player (AI is 'O')
        self.game = TicTacToe()
        self.ai = AIPlayer('O')

        # Initialize score tracking
        self.user_score = 0
        self.ai_score = 0
        self.draw_score = 0

        # Set up the UI background and layout
        self.root.config(bg="#EAEAEA")
        self.gradient_frame = tk.Frame(self.root, bg="#EAEAEA")
        self.gradient_frame.pack(fill="both", expand=True)

        # Create the game board (3x3 grid of buttons)
        self.buttons = []
        board_frame = tk.Frame(self.gradient_frame, bg="#EAEAEA")
        board_frame.pack(pady=20)

        button_size = 100  # Size of buttons on the board
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(board_frame, text="", font=('Helvetica', 20), width=5, height=2,
                                   bg="#282C34", fg="#ABB2BF", activebackground="#3E4451",
                                   activeforeground="#61AFEF", borderwidth=0,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

        # Status label for displaying current game status
        self.status_label = tk.Label(self.gradient_frame, text="Your move!", font=self.custom_font,
                                     bg="#EAEAEA", fg="#282C34", padx=10, pady=5)
        self.status_label.pack(pady=10)

        # Score labels for user, AI, and draws
        score_frame = tk.Frame(self.gradient_frame, bg="#EAEAEA")
        score_frame.pack(pady=10)

        self.user_score_label = tk.Label(score_frame, text=f"User: {self.user_score}", font=self.custom_font,
                                         bg="#EAEAEA", fg="#61AFEF", padx=10)
        self.user_score_label.grid(row=0, column=0, padx=20)

        self.ai_score_label = tk.Label(score_frame, text=f"AI: {self.ai_score}", font=self.custom_font,
                                       bg="#EAEAEA", fg="#E06C75", padx=10)
        self.ai_score_label.grid(row=0, column=1, padx=20)

        self.draw_score_label = tk.Label(score_frame, text=f"Draw: {self.draw_score}", font=self.custom_font,
                                         bg="#EAEAEA", fg="#98C379", padx=10)
        self.draw_score_label.grid(row=0, column=2, padx=20)

        # Reset button to reset scores
        self.reset_button = tk.Button(self.gradient_frame, text="Reset Scores", command=self.reset_scores,
                                      font=self.custom_font, bg="#C678DD", fg="#FFFFFF", activebackground="#BD93F9",
                                      borderwidth=0, padx=10, pady=5)
        self.reset_button.pack(pady=20)

        self.add_hover_effect()

    def center_window(self, width, height):
        # Centers the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.resizable(False, False)

    def add_hover_effect(self):
        # Adds hover effects for board buttons and reset button
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.bind("<Enter>", lambda e, b=button: b.config(bg="#61AFEF"))
                button.bind("<Leave>", lambda e, b=button: b.config(bg="#282C34"))

        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg="#BD93F9"))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg="#C678DD"))

    def on_click(self, row, col):
        # Handles player moves and updates the game state
        if self.game.board[row * 3 + col] == ' ' and self.game.current_winner is None:
            self.game.make_move(row * 3 + col, 'X')  # Player move
            self.update_buttons()

            if self.game.current_winner:  # Check if player wins
                self.user_score += 1
                self.update_scores()
                self.status_label.config(text="You win!")
                self.disable_buttons()
                self.root.after(2000, self.reset_board)
                return
            elif not self.game.empty_squares():  # Check for draw
                self.draw_score += 1
                self.update_scores()
                self.status_label.config(text="It's a draw!")
                self.disable_buttons()
                self.root.after(2000, self.reset_board)
                return

            # AI's turn
            self.status_label.config(text="AI is thinking...")
            self.disable_buttons()
            self.root.after(1000, self.ai_move)

    def ai_move(self):
        # AI makes its move and updates the game state
        square = self.ai.get_move(self.game)
        if square is not None:
            self.game.make_move(square, 'O')  # AI move
            row, col = divmod(square, 3)
            self.update_buttons()

            if self.game.current_winner:  # Check if AI wins
                self.ai_score += 1
                self.update_scores()
                self.status_label.config(text="AI wins!")
                self.disable_buttons()
                self.root.after(2000, self.reset_board)
                return
            elif not self.game.empty_squares():  # Check for draw
                self.draw_score += 1
                self.update_scores()
                self.status_label.config(text="It's a draw!")
                self.disable_buttons()
                self.root.after(2000, self.reset_board)
                return

        self.status_label.config(text="Your move!")
        self.enable_buttons()

    def update_buttons(self):
        # Updates the board UI based on the current game state
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game.board[row * 3 + col],
                                              state=tk.DISABLED if self.game.board[row * 3 + col] != ' ' else tk.NORMAL)

    def update_scores(self):
        # Updates the score display
        self.user_score_label.config(text=f"User: {self.user_score}")
        self.ai_score_label.config(text=f"AI: {self.ai_score}")
        self.draw_score_label.config(text=f"Draw: {self.draw_score}")

    def reset_scores(self):
        # Resets scores to zero and resets the board
        self.user_score = 0
        self.ai_score = 0
        self.draw_score = 0
        self.update_scores()
        self.reset_board()

    def reset_board(self):
        # Resets the board for a new game
        self.game.reset()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)
        self.status_label.config(text="Your move!")

    def disable_buttons(self):
        # Disables all board buttons
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def enable_buttons(self):
        # Enables all board buttons for available moves
        for row in range(3):
            for col in range(3):
                if self.game.board[row * 3 + col] == ' ':
                    self.buttons[row][col].config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()