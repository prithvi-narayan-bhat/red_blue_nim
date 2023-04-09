from argparse   import ArgumentParser as parser
from moves      import *


def gameEngine(redMarbleCount, blueMarbleCount, playerOne, searchDepth):
    turn = playerOne                                            # Set playerOne as input by user to start
    board = [redMarbleCount, blueMarbleCount]                   # Set up the gameBoard

    print(f"\n\nStarting board: {board}\n\n")                   # Display board

    while True:                                                 # Until there is a winner
        while board[0] > 0 and board[1] > 0:                    # Game ends when there are no more marbles on the board

            if board[0] == 0 or board[1] == 0:                  # Game ends
                break

            if turn == 'computer':                              # Get the computer's move
                board = getComputerMove(board, searchDepth)
            else:                                               # Get the human's move
                board = getHumanMove(board)

            print(f"\n\nCurrent board: {board}\n\n")            # Display the board after each turn
            turn = 'computer' if turn == 'human' else 'human'   # Update the player after each turn

        winner, score = evaluateBoardStatus(board, GET_SCORE)   # Get the score at the end of the game

        print(f"{winner} wins!\nScore: {score}")                # Print winner and the score

        break

if __name__ == '__main__':

    # Parse command line inputs from user
    cli = parser()
    cli.add_argument('red', help='Number of Red marbles')
    cli.add_argument('blue', help='Number of Blue marbles')
    cli.add_argument('playerOne', help='Player to make the first move: Human or Computer')
    cli.add_argument('searchDepth', help='Depth of the MinMax search')
    cli_args = cli.parse_args()

    redMarbleCount      = int(cli_args.red)
    blueMarbleCount     = int(cli_args.blue)
    playerOne           = cli_args.playerOne
    searchDepth         = int(cli_args.searchDepth)

    # Call function to start playing game
    gameEngine(redMarbleCount, blueMarbleCount, playerOne, searchDepth)
