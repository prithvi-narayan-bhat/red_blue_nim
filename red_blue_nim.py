import random
from copy import deepcopy

# Constants to represent the score multipliers for each color
RED_MULTIPLIER = 2
BLUE_MULTIPLIER = 3


class RedBlueNim:
    def __init__(self):
        # Initialize random number of red and blue marbles
        self.red_marbles = random.randint(1, 10)
        self.blue_marbles = random.randint(1, 10)

        self.current_player = 'computer'    # Set the current player to the computer
        self.game_over = False              # Set game_over flag to False

    def evaluate(self) -> int:
        # Evaluate the current state of the game and return a score
        if self.red_marbles == 0:
            # If the red pile is empty, return -3 times the number of blue marbles left
            return -3 * self.blue_marbles
        elif self.blue_marbles == 0:
            # If the blue pile is empty, return -2 times the number of red marbles left
            return -2 * self.red_marbles
        else:
            return 0                        # If both piles have marbles, return 0

    def get_possible_moves(self):
        # Get a list of all possible moves from the current state of the game
        possible_moves = []

        if self.red_marbles > 0:
            # If there are red marbles left, add all possible red moves to the list
            possible_moves += [(0, i) for i in range(1, self.red_marbles+1)]
        if self.blue_marbles > 0:
            # If there are blue marbles left, add all possible blue moves to the list
            possible_moves += [(1, i) for i in range(1, self.blue_marbles+1)]

        return possible_moves

    def display_board(self):
        # Print the current state of the game
        print(f"Red marbles: {self.red_marbles}")
        print(f"Blue marbles: {self.blue_marbles}")

    def get_player_move(self):
        # Get the move from the current player (human or computer)
        # If it's the human player, prompt for input
        if self.current_player == 'human':

            pile = input("\n\nChoose a pile (red or blue): ")

            while pile not in ['red', 'blue']:
                pile = input("Invalid input, choose a pile (red or blue): ")

            # Prompt user to input the number of marbles to remove
            count = input(f"How many {pile} marbles do you want to remove? ")

            while not count.isdigit() or int(count) < 1 or int(count) > getattr(self, f"{pile}_marbles"):
                count = input(
                    f"Invalid input, choose a number between 1 and {getattr(self, f'{pile}_marbles')}: ")

            count = int(count)

        # If it's the computer player, use MinMax with Alpha Beta Pruning to determine the best move
        else:
            pile, count = self.minmax_ab(
                depth=5, alpha=float('-inf'), beta=float('inf'))

            print(f"The computer chooses to remove {count} {pile} marble(s).")

        return pile, count

    def remove_marbles(self, pile, count):
	# Remove marbles from the specified pile
        if pile == 0:
            # If removing from the red pile, update the red_marbles attribute
            setattr(self, "red_marbles", getattr(self, "red_marbles") - count)
        else:
            # If removing from the blue pile, update the blue_marbles attribute
            setattr(self, "blue_marbles", getattr(
                self, "blue_marbles") - count)

        if self.red_marbles == 0 or self.blue_marbles == 0:
            self.game_over = True

    def minmax_ab(self, depth: int, alpha: float, beta: float) -> tuple[tuple[str, int], float]:
        if self.game_over or depth == 0:
            return None, self.evaluate()

        if self.current_player == 'computer':
            max_eval = float('-inf')

            for move in self.get_possible_moves():
                new_game = deepcopy(self)
                new_game.remove_marbles(move[0], move[1])
                value = new_game.minmax_ab(depth-1, alpha, beta)[1]

                if value > max_eval:
                    max_eval = value
                    best_move = move
                alpha = max(alpha, max_eval)

                if beta <= alpha:
                    break
            return best_move, max_eval

        else:
            min_eval = float('inf')

            for move in self.get_possible_moves():
                new_game = deepcopy(self)
                new_game.remove_marbles(move[0], move[1])
                value = new_game.minmax_ab(depth-1, alpha, beta)[1]

                if value < min_eval:
                    min_eval = value
                    best_move = move
                beta = min(beta, min_eval)

                if beta <= alpha:
                    break
            return best_move, min_eval


def play_game():
    game = RedBlueNim()

    while not game.game_over:
        game.display_board()
        pile, count = game.get_player_move()
        game.remove_marbles(pile, count)

        if not game.game_over:
            game.current_player = 'computer'
            pile, count = game.get_player_move()
            game.remove_marbles(pile, count)
            game.current_player = 'human'
    print("Game over!\n")

    if game.red_marbles == 0:
        print("The computer wins!\n\n")
        score = game.blue_marbles * BLUE_MULTIPLIER

    else:
        print("You win!\n")
        score = game.red_marbles * RED_MULTIPLIER
    print(f"Final score: {score}\n\n")


play_game()
