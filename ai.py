import logging
import math
import random

class AIPlayer:
    def __init__(self, letter, difficulty="hard"):
        self.letter = letter
        self.difficulty = difficulty

    def heuristic(self, state):
        """Evaluates board state for the medium difficulty level."""
        if state.current_winner == self.letter:
            return 1
        elif state.current_winner is not None:
            return -1
        else:
            # Score based on the number of potential two-in-a-row lines
            player_score = self.count_two_in_row(state, self.letter)
            opponent_score = self.count_two_in_row(state, 'X' if self.letter == 'O' else 'O')
            return player_score - opponent_score

    def count_two_in_row(self, state, letter):
        """Counts two-in-a-row lines with an empty spot for the specified letter."""
        count = 0
        for i in range(3):
            # Check rows and columns for two-in-a-row patterns
            if state.board[i * 3:(i + 1) * 3].count(letter) == 2 and ' ' in state.board[i * 3:(i + 1) * 3]:
                count += 1
            if [state.board[i + j * 3] for j in range(3)].count(letter) == 2 and ' ' in [state.board[i + j * 3] for j in range(3)]:
                count += 1
        # Check diagonals
        if [state.board[i] for i in [0, 4, 8]].count(letter) == 2 and ' ' in [state.board[i] for i in [0, 4, 8]]:
            count += 1
        if [state.board[i] for i in [2, 4, 6]].count(letter) == 2 and ' ' in [state.board[i] for i in [2, 4, 6]]:
            count += 1
        return count
   
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