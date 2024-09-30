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
        return 0

    if is_maximizing:
        best_value = -math.inf
        for move in state.available_moves():
            state.make_move(move, self.letter)
            sim_score = self.minimax(state, depth + 1, alpha, beta, False)
            state.board[move] = ' '
            state.current_winner = None
            best_value = max(best_value, sim_score)
            alpha = max(alpha, sim_score)
            if beta <= alpha:
                break
        return best_value
    
    else:
        best_value = math.inf
        opponent = 'O' if self.letter == 'X' else 'X'
        for move in state.available_moves():
            state.make_move(move, opponent)
            sim_score = self.minimax(state, depth + 1, alpha, beta, True)
            state.board[move] = ' '
            state.current_winner = None
            best_value = min(best_value, sim_score)
            beta = min(beta, sim_score)
            if beta <= alpha:
                break
        return best_value