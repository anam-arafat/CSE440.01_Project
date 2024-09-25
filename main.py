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

        self.buttons = [tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2, command=lambda i=i: self.on_button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)
