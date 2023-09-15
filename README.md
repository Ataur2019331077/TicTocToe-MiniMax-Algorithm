# Tic-Tac-Toe with Minimax Algorithm

In this document, we explore how to implement the Tic-Tac-Toe game and use the Minimax algorithm to create an optimal player.

## Tic-Tac-Toe Game

Tic-Tac-Toe, also known as "Noughts and Crosses," is a classic two-player game played on a 3x3 grid. The goal is to be the first to place three of your marks (either 'X' or 'O') in a row, column, or diagonal.

### Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their mark ('X' or 'O') in an empty cell.
- The game ends when one player has three marks in a row, column, or diagonal, or when all cells are filled.
- If all cells are filled and no player has won, the game is a draw.

## Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used in two-player games with perfect information, like Tic-Tac-Toe. It works as follows:

1. **Player Max (e.g., 'X'):** Maximizes the score.
2. **Player Min (e.g., 'O'):** Minimizes the score.

The algorithm explores the game tree by considering all possible moves and outcomes. It assigns a score to each terminal state (win, lose, draw) and selects the move that leads to the best score for Player Max while assuming Player Min makes optimal moves.

### Pseudocode for Minimax

Here is a simplified pseudocode for the Minimax algorithm in the context of Tic-Tac-Toe:

```plaintext
function minimax(board, depth, isMaximizingPlayer):
    if the game is over:
        return score of the board
    
    if isMaximizingPlayer:
        bestScore = -Infinity
        for each empty cell on the board:
            make a move in the cell for the maximizing player
            score = minimax(board, depth + 1, false)
            undo the move
            bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = +Infinity
        for each empty cell on the board:
            make a move in the cell for the minimizing player
            score = minimax(board, depth + 1, true)
            undo the move
            bestScore = min(bestScore, score)
        return bestScore

