# red_blue_nim
A simple program to play the NIM game with a computer

## Author
* Prithvi Bhat | 1002033598
* +1(682)340-1126
* pnb3598@mavs.uta.edu


This code code is available on Github at the following link
#### https://github.com/prithvi-narayan-bhat/red_blue_nim

To clone the repository, enter the follwoing command on a Git supported machine
#### git clone git@github.com:prithvi-narayan-bhat/red_blue_nim.git


## Execution
### System Requirements
The project was developed and tested on a Linux Mint machine (Kernel 5.15.0-56-generic) with Python3 (Version 3.10.6).
However, I am positive it can be run without any modifications on any compatible system
### Required Files
Ensure the the following files are all present in the same directory when executing
1. red_blue_nim.py
2. moves.py
3. gameEngine.py


### Command Line Execution
Enter the following to view the CLI help interface
##### python3 red_blue_nim.py -h [--help]

To run the application and perform any particular algorithm, run the following
##### python3 expense_8_puzzle.py [number_of_red_marbles] [number_of_blue_marbles] [first_player] [depth_of_search]
### [number_of_red_marbles]
This can be any positive integer

### [number_of_blue_marbles]
This can be any positive integer

### [first_player]
This can be one two values 'human' or 'computer'

## Minmax Algorithm

The evaluateMoves function implements depth limited Minimax algorithm with alpha-beta pruning to determine the best move for the computer in this game.

#### Control Dependencies
The function decides on the move depending on the following:
1. current state of game
2. current depth in the search tree
3. alpha value (for pruning)
4. beta value (for pruning)
5. bool value (indicates if current player is maximizing or not)

#### Exit Condition
The algorithm stops or exits on meeting one of the following conditions:
1. maximum depth is reached
2. either one or both of the stack of red or blue marbles are empty

Upon the conditions being satisfied, the algorithm returns the state of the board, as determined by evaluateBoardStatus() function.

The abPruneValue variable is initialized to negative infinity if a max player is playing. The algorithm then iterates through both piles of marbles to find the best move. A new board is created each time a marble is removed, and the evaluateMoves function is recursively called with
1. the new game board,
2. reduced depth,
3. updated alpha, beta, and
4. the maximizing player value set to False

It then updates the abPruneValue variable with the maximum of the current abPruneValue and the returned value from the recursive call. It also updates the alpha value if the abPruneValue is greater than alpha. If beta is less than or equal to alpha, it breaks out of the loop.

The algorithm initializes abPruneValue to positive infinity if the min player is playing and follows the same process as the maximizing player.
The only difference being with the abPruneValue initialized to positive infinity and taking the minimum of the current abPruneValue and the returned value from the recursive call. It also updates the beta value if value is less than beta. If beta is less than or equal to alpha, it breaks out of the loop.

Finally, the function returns the abPruneValue variable which represents the best score the maximizing player can achieve in the current state of the game.


## Eval Function

The evaluateBoardStatus function is invoked to calculate the score of the game or the current status of the game.

Depending on the arguments, the function returns
1. the intermediary status of the board as the sum of the product of the red marbles and "2", and the product of the blue marbles and the "3".
or
2. Determines the winner of the game and their score