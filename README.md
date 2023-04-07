# red_blue_nim
A simple program to play the NIM game with a computer


## Minmax Algorithm

The minmax_ab function implements the Minimax algorithm with alpha-beta pruning to determine the best move for the computer in this game.

The function makes a decision on the move to be made depending on the current state of game, the current depth in the search tree, alpha and beta values for pruning, and a bool value indicating if the current player is maximizing or not.

If the function reaches the maximum depth or if either one or both of the stack of red or blue marbles are empty, it returns the evaluation of the board, which is determined by the evaluate function.

If a max player is playing, it initializes the value to negative infinity, and iterates through both piles of marbles to find the best move. Each time a marble is removed, a new board is created, and the minmax_ab function is recursively called with the new game board, reduced depth, updated alpha, beta, and with the maximizing player value set to False. It then updates the value variable with the maximum of the current value and the returned value from the recursive call. It also updates the alpha value if the value is greater than alpha. If beta is less than or equal to alpha, it breaks out of the loop.

If the min player is playing, the algorithm initializes value to positive infinity and follows the same process as the maximizing player, but with the value initialized to positive infinity and taking the minimum of the current value and the returned value from the recursive call. It also updates the beta value if value is less than beta. If beta is less than or equal to alpha, it breaks out of the loop.

Finally, the function returns the value variable which represents the best score the maximizing player can achieve in the current state of the game.