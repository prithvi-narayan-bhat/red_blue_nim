import sys
import random

# Constants to represent the score multipliers
RED = 2
BLUE = 3

def evaluateBoardStatus(gameBoard, winner):
    """
        Function to evaluate current state of the gameBoard
    """
    red_count, blue_count = gameBoard                   # Update marble counts from present Board

    if (winner == 'minimax'):
        return RED * red_count + BLUE * blue_count      # Return present intermediary status of the board

    elif (winner == 'score'):
        if (gameBoard[0] == 0):                         # Implies the computer has won
            score = gameBoard[1] * BLUE                 # Calculate score
            return 'Computer', score                    # Return score and winner
        else:                                           # Implies Human player has won
            score = gameBoard[1] * RED                  # Calculate score
            return 'Human', score                       # Return winner and score


def minimax_ab(gameBoard, searchDepth, alpha, beta, maxPlayer):
    """
        Function to determine the computer's next move using the minimax alpha-beta pruning
    """
    if searchDepth == 0 or gameBoard[0] == 0 or gameBoard[1] == 0:
        return evaluateBoardStatus(gameBoard, 'minimax')   # Return the intermediary state if maximum depth has been reached or Board is empty

    if maxPlayer:
        abPruneValue = float('-inf')                    # Set initial min value to -infinity

        for i in range(2):                              # Maximum number of marbles of concern

            if gameBoard[i] > 0:                        # Process only if Board not empty
                updatedBoard = list(gameBoard)
                updatedBoard[i] -= 1                    # Decrement one instance from the game gameBoard

                abPruneValue = max(
                    abPruneValue,
                    minimax_ab(
                        updatedBoard,
                        searchDepth-1,
                        alpha,
                        beta,
                        False)
                )

                alpha = max(alpha, abPruneValue)    # Update alpha as the maximum

                if beta <= alpha:                   # Exit condition
                    break

        return abPruneValue

    else:
        abPruneValue = float('inf')                 # Set initial max value to +infinity

        for i in range(2):                          # Only two possible values in pile

            if gameBoard[i] > 0:                    # Process only if gameBoard not empty
                updatedBoard = list(gameBoard)
                updatedBoard[i] -= 1                # Decrement one instance from the game gameBoard

                abPruneValue = min(
                    abPruneValue,
                    minimax_ab(
                    updatedBoard,
                    searchDepth-1,
                    alpha,
                    beta,
                    True)
                )

                beta = min(beta, abPruneValue)      # Update beta as the minimum

                if beta <= alpha:                   # Exit condition
                    break

        return abPruneValue