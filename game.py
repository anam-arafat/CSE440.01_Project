class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board in a 1D list
        self.current_winner = None  # Tracks the winner
    def print_board(self):
        # Print the game board
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        # Tells the players where they can mark (0 to 8)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    def available_moves(self):
        # Returns a list of available spots on the board
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        # Checks if there are empty squares
        return ' ' in self.board

