import math

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

def minimax(self, state, depth, alpha, beta, is_maximizing):
    if state.current_winner == 'X':
        return 1 if self.letter == 'X' else -1
    elif state.current_winner == 'O':
        return 1 if self.letter == 'O' else -1
    elif state.empty_squares() == False:
        return 0  # It's a tie

    if is_maximizing:
        max_eval = -math.inf
        for move in state.available_moves():    
            state.make_move(move, self.letter)
            sim_score = self.minimax(state, depth + 1, alpha, beta, False)
            state.board[move] = ' '
            state.current_winner = None
            max_eval = max(max_eval, sim_score)
            alpha = max(alpha, sim_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        opponent = 'O' if self.letter == 'X' else 'X'
        for move in state.available_moves():
            state.make_move(move, opponent)
            sim_score = self.minimax(state, depth + 1, alpha, beta, True)
            state.board[move] = ' '
            state.current_winner = None
            min_eval = min(min_eval, sim_score)
            beta = min(beta, sim_score)
            if beta <= alpha:
                break
        return min_eval

