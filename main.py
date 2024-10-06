import tkinter as tk
from tkinter import messagebox
from game import TicTacToe
from ai import AIPlayer

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.ai = AIPlayer('O')
        self.root = root
        self.root.title("Tic Tac Toe")

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2)
            button.config(command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def on_button_click(self, i):
        if self.game.board[i] == ' ' and not self.game.current_winner:
            self.game.make_move(i, 'X')
            self.buttons[i].config(text='X')
            if self.game.current_winner:
                messagebox.showinfo("Game Over", "Player X wins!")
            elif self.game.empty_squares():
                self.ai_move()
                if self.game.current_winner:
                    messagebox.showinfo("Game Over", "Player O wins!")
                    
    def ai_move(self):
        if self.game.empty_squares():
            move = self.ai.best_move(self.game)
            if move is not None:
                self.game.make_move(move, 'O')
                self.buttons[move].config(text='O')

    def reset_game(self):
        self.game.reset()
        for button in self.buttons:
            button.config(text=' ')
        self.ai = AIPlayer('O')

    def on_button_click(self, i):
        if self.game.board[i] == ' ' and not self.game.current_winner:
            self.game.make_move(i, 'X')
            self.buttons[i].config(text='X')
            if self.game.current_winner:
                messagebox.showinfo("Game Over", "Player X wins!")
            elif self.game.empty_squares():
                self.ai_move()
                if self.game.current_winner:
                    messagebox.showinfo("Game Over", "Player O wins!")
                elif not self.game.empty_squares():
                    messagebox.showinfo("Game Over", "It's a tie!")
        self.ai = AIPlayer('O')


    


