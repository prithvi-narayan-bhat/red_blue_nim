import random
from argparse import ArgumentParser as parser
from auxillary import *
from moves import *


def gameEngine(redMarbleCount, blueMarbleCount, playerOne, searchDepth):
    current_player = playerOne
    board = [redMarbleCount, blueMarbleCount]

    while True:

        while board[0] > 0 and board[1] > 0:
            print(f"\n\nCurrent board: {board}\n")

            if current_player == 'computer':
                board, removed_color, removed_count = getComputerMove(board, searchDepth)
                print(f"Computer removes {removed_count} {removed_color} marble(s)")

                if board[0] == 0 or board[1] == 0:
                    break

            else:
                board, marble, count = getHumanMove(board)
                print(f"You removed {count} {marble} marble(s)")

            current_player = 'computer' if current_player == 'human' else 'human'

        winner, score = evaluateBoardStatus(board, 'score')
        print(f"{winner} wins!\nScore: {score}")

        break

if __name__ == '__main__':

    cli = parser()
    cli.add_argument('red', help='Number of Red marbles')
    cli.add_argument('blue', help='Number of Blue marbles')
    cli.add_argument('playerOne', help='Player to make the first move: Human or Computer')
    cli.add_argument('searchDepth', help='Depth of the MinMax search')
    cli_args = cli.parse_args()

    redMarbleCount       = int(cli_args.red)
    blueMarbleCount       = int(cli_args.blue)
    playerOne    = cli_args.playerOne
    searchDepth    = int(cli_args.searchDepth)

    gameEngine(redMarbleCount, blueMarbleCount, playerOne, searchDepth)
