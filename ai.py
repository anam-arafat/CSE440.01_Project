import math

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter  # AI's letter ('X' or 'O')
    
    def heuristic(self, state):
        """
        Evaluates the board state and returns a score based on the AI's advantage.
        """
        opponent = 'O' if self.letter == 'X' else 'X'
        score = 0

        # Winning line patterns
        winning_lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for line in winning_lines:
            ai_count = sum([1 for i in line if state.board[i] == self.letter])
            opponent_count = sum([1 for i in line if state.board[i] == opponent])
            empty_count = sum([1 for i in line if state.board[i] == ' '])

            # AI advantage
            if ai_count == 2 and empty_count == 1:
                score += 10  # AI is one move away from winning
            elif ai_count == 1 and empty_count == 2:
                score += 1  # AI has potential to set up a win

            # Opponent threat
            if opponent_count == 2 and empty_count == 1:
                score -= 8  # Opponent is one move away from winning
            elif opponent_count == 1 and empty_count == 2:
                score -= 1  # Opponent has potential to set up a win

            # Uncomment for balanced strategy
            # if ai_count == 1 and opponent_count == 1 and empty_count == 1:
            #     score += 2  # Balance both defense and offense

        return score

    def minimax(self, state, depth, alpha, beta, is_maximizing):
        # Base case: Check for terminal state (win, lose, or tie)
        if state.current_winner == self.letter:
            return 100 - depth  # Prioritize faster wins
        elif state.current_winner == ('O' if self.letter == 'X' else 'X'):
            return -100 + depth  # Penalize slower losses
        elif not state.empty_squares():
            return 0  # Tie game

        if depth > 3:  # Limit depth for performance (optional)
            return self.heuristic(state)

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
        """
        Returns the best move based on the selected difficulty level.
        """

        # Easy difficulty: Random move
        # import random
        # return random.choice(game.available_moves())

        # Medium difficulty: Limited heuristic evaluation
        # best_move = None
        # best_score = -math.inf
        # for move in game.available_moves():
        #     game.make_move(move, self.letter)
        #     score = self.heuristic(game)
        #     game.board[move] = ' '  # Undo move
        #     game.current_winner = None  # Reset winner
        #     if score > best_score:
        #         best_score = score
        #         best_move = move
        # return best_move

        # Hard difficulty: Full Minimax with alpha-beta pruning
        best_move = None
        best_score = -math.inf
        for move in game.available_moves():
            game.make_move(move, self.letter)
            score = self.minimax(game, 0, -math.inf, math.inf, False)
            game.board[move] = ' '  # Undo move
            game.current_winner = None  # Reset winner
            if score > best_score:  # Update best move if a better score is found
                best_score = score
                best_move = move
        return best_move
