import tkinter as tk
from tkinter import font as tkfont
from game import TicTacToe
from ai import AIPlayer
from tkinter import messagebox, simpledialog

class TicTacToeGUI:
    def __init__(self, root):
        ...
        self.select_difficulty()

    def select_difficulty(self):
        # Use a dropdown to ensure valid difficulty selection
        difficulty = simpledialog.askstring("Select Difficulty", "Choose difficulty: Easy, Medium, or Hard")
        difficulty = difficulty.lower() if difficulty else "hard"  # Default to hard if input is None or empty
        if difficulty == "easy":
            self.ai = AIPlayer('O', difficulty="easy")
        elif difficulty == "medium":
            self.ai = AIPlayer('O', difficulty="medium")
        else:
            self.ai = AIPlayer('O', difficulty="hard")
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
        self.select_difficulty()
    
    def select_difficulty(self):
        difficulty = messagebox.askquestion("Select Difficulty", "Choose difficulty: Easy, Medium, or Hard")
        # Default to hard if invalid input is provided
        if difficulty == "easy":
            self.ai = AIPlayer('O', difficulty="easy")
        elif difficulty == "medium":
            self.ai = AIPlayer('O', difficulty="medium")
        else:
            self.ai = AIPlayer('O', difficulty="hard")

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
