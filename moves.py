from auxillary import *

def getComputerMove(gameBoard, searchDepth):
    """
        Function to determine the computer's next move using minimax and alpha-beta pruning
    """
    bestRemoveValue = float('-inf')                                                     # Set an absurdly large value at first
    bestMoveList = []                                                                   # Initialise an empty list
    removeCount = 0                                                                     # Initialise value
    removeColor = ''                                                                    # Initialise empty string

    for i in range(2):

        if gameBoard[i] > 0:
            updatedBoard = list(gameBoard)
            updatedBoard[i] -= 1

            value = minimax_ab(
                updatedBoard,
                searchDepth-1,
                float('-inf'),
                float('inf'),
                False
            )

            if value > bestRemoveValue:
                bestRemoveValue = value
                bestMoveList = [i]
                removeColor = 'red' if i == 0 else 'blue'
                removeCount = gameBoard[i] - updatedBoard[i]

            elif value == bestRemoveValue:
                bestMoveList.append(i)

    optimalMove = random.choice(bestMoveList)
    gameBoard[optimalMove] -= 1

    return gameBoard, removeColor, removeCount


def getHumanMove(gameBoard):
    """
        Function to read human player's move and validate it
    """

    marble = input("Choose a marble to remove from (red/blue): ")                       # Prompt player for an input

    marbleColour = 0 if marble.lower() == 'red' else 1                                  # Parse input

    while True:
        removeCount = input("Choose how many marbles to remove (1 or 2): ")             # Prompt player for an input
        try:
            removeCount = int(removeCount)                                              # Parse input

            if removeCount < 1 or removeCount > 2:                                      # Validate input
                print("ERROR! Invalid value\n\n\n")
                continue

            if gameBoard[marbleColour] < removeCount:                                   # Validate input
                print(f"ERROR! Invalid value")
                print("Enter a number smaller than {gameBoard[marbleColour]}: ")        # Prompt user for an input
                continue
            break

        except ValueError:
            print("ERROR! Invalid value\n\n\n")                                         # Throw exception
            continue

    gameBoard[marbleColour] -= removeCount                                              # Remove the user input number of marbles of user input colour

    return gameBoard, marble, removeCount                                               # Return updated values
