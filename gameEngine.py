# Constants to represent the score multipliers
RED_MULTIPLIER = 2
BLU_MULTIPLIER = 3
MAX_MARBLES = 2
MINUS_INFINITY = -1000000000000
PLUS__INFINITY = 10000000000000

GET_SCORE   = 1
GET_STATE   = 0

def evaluateBoardStatus(gameBoard, task):
    """
        Function to evaluate current state of the gameBoard
    """
    red_count, blue_count = gameBoard                           # Update marble counts from present Board

    if (task == GET_STATE):                                     # Return present intermediary status of the board
        return RED_MULTIPLIER * red_count + BLU_MULTIPLIER * blue_count

    elif (task == GET_SCORE):
        if (gameBoard[0] == 0):                                 # Implies the computer has won
            score = gameBoard[1] * BLU_MULTIPLIER               # Calculate score
            return 'Computer', score                            # Return score and winner
        else:                                                   # Implies Human player has won
            score = gameBoard[1] * RED_MULTIPLIER               # Calculate score
            return 'Human', score                               # Return winner and score


def evaluateMoves(gameBoard, searchDepth, alpha, beta, maxPlayer):
    """
        Function to determine the computer's next move using the minimax alpha-beta pruning
    """

    if searchDepth == 0 or gameBoard[0] == 0 or gameBoard[1] == 0:
        return evaluateBoardStatus(gameBoard, GET_STATE)        # Return the intermediary state if maximum depth has been reached or Board is empty

    if maxPlayer:
        abPruneValue = int(MINUS_INFINITY)                      # Set initial min value to -infinity

        for i in range(MAX_MARBLES):                            # Maximum number of marbles of concern

            if gameBoard[i] > 0:                                # Process only if Board not empty
                updatedBoard = list(gameBoard)
                updatedBoard[i] -= 1                            # Decrement one instance from the game gameBoard

                abPruneValue = max (abPruneValue, evaluateMoves( updatedBoard, searchDepth-1, alpha, beta, False))

                alpha = max(alpha, abPruneValue)                # Update alpha as the maximum

                if beta <= alpha:                               # Exit condition
                    break

    else:
        abPruneValue = int(PLUS__INFINITY)                      # Set initial max value to +infinity

        for i in range(MAX_MARBLES):                            # Only two possible values in pile

            if gameBoard[i] > 0:                                # Process only if gameBoard not empty
                updatedBoard = list(gameBoard)
                updatedBoard[i] -= 1                            # Decrement one instance from the game gameBoard

                abPruneValue = min (abPruneValue, evaluateMoves( updatedBoard, searchDepth-1, alpha, beta, True))

                beta = min(beta, abPruneValue)                  # Update beta as the minimum

                if beta <= alpha:                               # Exit condition
                    break

    return abPruneValue