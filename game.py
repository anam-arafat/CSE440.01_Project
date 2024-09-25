class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board in a 1D list
        self.current_winner = None  # Tracks the winner