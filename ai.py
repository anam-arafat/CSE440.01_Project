def minimax(self, state, depth, alpha, beta, is_maximizing):
    # Determine if the game has reached a terminal state
    if state.current_winner == 'X':
        return 1 if self.letter == 'X' else -1
    elif state.current_winner == 'O':
        return 1 if self.letter == 'O' else -1
    elif state.empty_squares() == False:
        return 0  # It's a tie

    # If we're maximizing, find the best score for 'X'
    if is_maximizing:
        best_score = -math.inf
        for move in state.available_moves():
            state.make_move(move, self.letter)
            score = self.minimax(state, depth + 1, alpha, beta, False)
            state.undo_move(move)  # Undo the move
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score

    # If we're minimizing, find the best score for 'O'
    else:
        best_score = math.inf
        for move in state.available_moves():
            state.make_move(move, 'O' if self.letter == 'X' else 'X')
            score = self.minimax(state, depth + 1, alpha, beta, True)
            state.undo_move(move)  # Undo the move
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score
