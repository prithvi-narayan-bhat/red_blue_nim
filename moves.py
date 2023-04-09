from gameEngine import *
import random

REMOVE_MARBLE = 1


def getComputerMove(gameBoard, searchDepth):
    """
        Function to determine the computer's next move using minimax and alpha-beta pruning
    """
    coloursToRemove = int(MINUS_INFINITY)                                   # Set an absurdly large abPruneValue at first. Implying, not moving at all
    bestMoveList = []                                                       # Initialise an empty list of best moves
    removedColour = ''                                                      # Initialise empty string of removed marble

    for i in range(MAX_MARBLES):

        updatedBoard = list(gameBoard)                                      # Take a local copy of the gameBoard to determine the best move

        while updatedBoard[i] > 0:                                          # While the game still has possible moves to make

            updatedBoard[i] -= REMOVE_MARBLE                                # Indicate that one move has be made, to update the loop exit condition

            # Call the minimax function repeatedly for each colour to determine the feasibility of the move
            abPruneValue = evaluateMoves(updatedBoard, searchDepth-1, float('-inf'), float('inf'), False)

            if abPruneValue >= coloursToRemove:                             # Implies it is a better move than not moving at all
                coloursToRemove = abPruneValue
                bestMoveList.append(i)                                      # Append the move to a list of possible moves


    optimalMove = random.choice(bestMoveList)                               # Pick a random move from the most optimal moves
    removedColour = 'red' if optimalMove == 0 else 'blue'                   # Return the removed colour to be printed

    gameBoard[optimalMove] -= REMOVE_MARBLE                                 # Indicate that the game has one lesser move

    print(f"Computer removes a {removedColour} marble")

    return gameBoard


def getHumanMove(gameBoard):
    """
        Function to read human player's move and validate it
    """
    removedColour = input("Choose a marble to remove from (red/blue): ")    # Prompt player for an input
    marbleColour = 0 if removedColour.lower() == 'red' else 1               # Parse input

    gameBoard[marbleColour] -= REMOVE_MARBLE                                # Remove the user input number of marbles of user input colour

    return gameBoard                                                        # Return updated values
