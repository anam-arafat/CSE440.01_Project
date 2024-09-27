def minimax(self, state, depth, alpha, beta, is_maximizing):
        # Check for terminal state
        if state.current_winner == 'X':
            return 1 if self.letter == 'X' else -1
        elif state.current_winner == 'O':
            return 1 if self.letter == 'O' else -1
        elif not state.empty_squares():
            return 0  # Tie
