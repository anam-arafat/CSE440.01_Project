class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board in a 1D list
        self.current_winner = None  # Tracks the winner
     def reset(self):
        # Resets the game board for a new game
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """Prints the current game board."""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """Prints the board numbers."""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """Returns a list of available spots on the board."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """Checks if there are empty squares."""
        return ' ' in self.board

    def num_empty_squares(self):
        """Counts empty squares."""
        return self.board.count(' ')

    def make_move(self, square, letter):
        """Marks the board if valid move."""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """Checks for the winning condition."""
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def reset(self):
        """Resets the game board for a new game."""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


