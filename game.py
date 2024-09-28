class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board in a 1D list
        self.current_winner = None  # Tracks the winner
        def print_board(self):
        # Print the game board
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
