# Tic-Tac-Toe AI: Implement an AI Agent That Plays Tic-Tac-Toe Optimally

This project implements an AI agent that plays Tic-Tac-Toe using game tree search algorithms like Minimax with Alpha-Beta pruning. The goal is to explore different heuristic functions and improve the AI's performance in Tic-Tac-Toe.

## Features

- **Graphical User Interface (GUI)**: A clean and interactive UI built with Tkinter.
- **AI Player**: The AI uses the Minimax algorithm with Alpha-Beta pruning for optimal performance.
- **Score Tracking**: Keeps track of user wins, AI wins, and draws.
- **Reset Scores**: Users can reset the scores at any time.
- **Heuristic Functions**: The project includes exploration of different heuristic functions to enhance the AI's decision-making process.

## Game Description

- The game starts with the player (who plays as **X**) making their move.
- After each player move, the AI (playing as **O**) calculates its best move using the Minimax algorithm.
- The game continues until there is a winner or the game results in a draw.
- Scores are displayed for the player, AI, and draws.
- You can reset the scores by clicking the "Reset Scores" button.

## Project Structure

- `main.py`: This file contains the logic for the GUI and user interactions.
- `ai.py`: This file implements the AI player using the Minimax algorithm with Alpha-Beta pruning.
- `game.py`: This file defines the core mechanics of the Tic-Tac-Toe game (board state, move validation, checking for winners, etc.).

## AI Logic (Minimax Algorithm)

The AI uses the Minimax algorithm with Alpha-Beta pruning to evaluate all possible moves and select the optimal one. The AI is guaranteed to never lose, but the player can still force a draw with perfect play.

### Minimax Details:

- **Maximizing Player (AI)**: The AI tries to maximize its chances of winning by evaluating the board state.
- **Minimizing Player (Human)**: The player tries to minimize the AI's chances by selecting moves that reduce the AI's advantage.
- **Alpha-Beta Pruning**: This optimization reduces the number of board states the AI needs to evaluate, improving performance.

### Heuristic Functions:

As part of the exploration, different heuristic functions are examined to improve the AI's performance beyond the default game state evaluations. These heuristics allow the AI to prioritize certain moves and make quicker decisions.

## Prerequisites

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Ensure you have Tkinter installed. On most systems, Tkinter comes pre-installed with Python, but if it's missing, you can install it via:

    **For MacOS:**
    Tkinter should be included with Python, but you can reinstall Python using Homebrew to ensure it's included:
    ```bash
    brew install python
    ```

    **For Windows:**
    Tkinter is usually included with Python installations. No extra steps are required.

## How to Run

1. Navigate to the project directory.
2. Run the game by executing:
    ```bash
    python main.py
    ```
