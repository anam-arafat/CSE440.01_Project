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
def best_move(self, state):
        best_move = None
        best_value = -math.inf if self.letter == 'X' else math.inf
        for move in state.available_moves():
            state.make_move(move, self.letter)
            move_value = self.minimax(state, 0, -math.inf, math.inf, self.letter == 'O')
            state.board[move] = ' '
            state.current_winner = None
            if (self.letter == 'X' and move_value > best_value) or (self.letter == 'O' and move_value < best_value):
                best_value = move_value
                best_move = move
        return best_move
import logging

logging.basicConfig(level=logging.DEBUG)

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def minimax(self, state, depth, alpha, beta, is_maximizing):
        if state.current_winner == 'X':
            return 1 if self.letter == 'X' else -1
        elif state.current_winner == 'O':
            return 1 if self.letter == 'O' else -1
        elif not state.empty_squares():
            return 0
        
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

    def best_move(self, state):
        best_move = None
        best_value = -math.inf if self.letter == 'X' else math.inf
        for move in state.available_moves():
            state.make_move(move, self.letter)
            move_value = self.minimax(state, 0, -math.inf, math.inf, self.letter == 'O')
            state.board[move] = ' '
            state.current_winner = None
            if (self.letter == 'X' and move_value > best_value) or (self.letter == 'O' and move_value < best_value):
                best_value = move_value
                best_move = move
        return best_move
