import logging

import math

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter  # AI's letter ('X' or 'O')
   
    def minimax(self, state, depth, alpha, beta, is_maximizing):
        # Base case: Check for terminal state (win, lose, or tie)
        if state.current_winner == 'X':
            return 1 if self.letter == 'X' else -1
        elif state.current_winner == 'O':
            return 1 if self.letter == 'O' else -1
        elif not state.empty_squares():
            return 0  # Tie game

        if is_maximizing:
            max_eval = -math.inf  # Maximizing player (AI)
            for move in state.available_moves():
                state.make_move(move, self.letter)
                sim_score = self.minimax(state, depth + 1, alpha, beta, False)
                state.board[move] = ' '  # Undo move
                state.current_winner = None  # Reset winner
                max_eval = max(max_eval, sim_score)
                alpha = max(alpha, sim_score)
                if beta <= alpha:  # Alpha-beta pruning
                    break
            return max_eval
        else:
            min_eval = math.inf  # Minimizing player (opponent)
            opponent = 'O' if self.letter == 'X' else 'X'
            for move in state.available_moves():
                state.make_move(move, opponent)
                sim_score = self.minimax(state, depth + 1, alpha, beta, True)
                state.board[move] = ' '  # Undo move
                state.current_winner = None  # Reset winner
                min_eval = min(min_eval, sim_score)
                beta = min(beta, sim_score)
                if beta <= alpha:  # Alpha-beta pruning
                    break
            return min_eval
   
    def get_move(self, game):
        # Find the best possible move for AI
        best_move = None
        best_score = -math.inf
        for possible_move in game.available_moves():
            game.make_move(possible_move, self.letter)
            score = self.minimax(game, 0, -math.inf, math.inf, False)
            game.board[possible_move] = ' '  # Undo move
            game.current_winner = None  # Reset winner
            if score > best_score:  # Update best move if a better score is found
                best_score = score
                best_move = possible_move
        return best_move


logging.basicConfig(level=logging.DEBUG)