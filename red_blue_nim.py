import random

RED_MULTIPLIER = 2
BLUE_MULTIPLIER = 3


class RedBlueNim:
    def __init__(self):
        self.red_marbles = random.randint(1, 10)
        self.blue_marbles = random.randint(1, 10)
        self.current_player = 'computer'
        self.game_over = False

    def evaluate(self) -> int:
        if self.red_marbles == 0:
            return -3 * self.blue_marbles
        elif self.blue_marbles == 0:
            return -2 * self.red_marbles
        else:
            return 0

    def display_board(self):
        print(f"Red marbles: {self.red_marbles}")
        print(f"Blue marbles: {self.blue_marbles}")

    def get_player_move(self):
        if self.current_player == 'human':
            pile = input("Choose a pile (red or blue): ")
            while pile not in ['red', 'blue']:
                pile = input("Invalid input, choose a pile (red or blue): ")
            count = input(f"How many {pile} marbles do you want to remove? ")
            while not count.isdigit() or int(count) < 1 or int(count) > getattr(self, f"{pile}_marbles"):
                count = input(
                    f"Invalid input, choose a number between 1 and {getattr(self, f'{pile}_marbles')}: ")
            count = int(count)
        else:
            # Use MinMax with Alpha Beta Pruning to determine the best move
            pile, count = self.minmax_ab()
            print(f"The computer chooses to remove {count} {pile} marble(s).")
        return pile, count

    def remove_marbles(self, pile, count):
        setattr(self, f"{pile}_marbles", getattr(
            self, f"{pile}_marbles") - count)
        if self.red_marbles == 0 or self.blue_marbles == 0:
            self.game_over = True

    def minmax_ab(self, depth=3, alpha=-float('inf'), beta=float('inf')):
        if depth == 0 or self.game_over:
            return None, self.evaluate()

        if self.current_player == 'computer':
            max_value = -float('inf')
            best_move = None
            for pile in ['red', 'blue']:
                for count in range(1, getattr(self, f"{pile}_marbles")+1):
                    new_game = RedBlueNim()
                    new_game.red_marbles = self.red_marbles
                    new_game.blue_marbles = self.blue_marbles
                    new_game.current_player = 'human'
                    new_game.game_over = self.game_over
                    new_game.remove_marbles(pile, count)
                    value = new_game.minmax_ab(depth-1, alpha, beta)[1]
                    if value > max_value:
                        max_value = value
                        best_move = (pile, count)
                    alpha = max(alpha, max_value)
                    if beta <= alpha:
                        break
            return best_move
        else:
            min_value = float('inf')
            best_move = None
            for pile in ['red', 'blue']:
                for count in range(1, getattr(self, f"{pile}_marbles")+1):
                    new_game = RedBlueNim()
                    new_game.red_marbles = self.red_marbles
                    new_game.blue_marbles = self.blue_marbles
                    new_game.current_player = 'computer'
                    new_game.game_over = self.game_over
                    new_game.remove_marbles(pile, count)
                    value = new_game.minmax_ab(depth-1, alpha, beta)[1]
                    if value < min_value:
                        min_value = value
                        best_move = (pile, count)
                    beta = min(beta, min_value)


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
    print("Game over!")
    if game.red_marbles == 0:
        print("The computer wins!")
        score = game.blue_marbles * BLUE_MULTIPLIER
    else:
        print("You win!")
        score = game.red_marbles * RED_MULTIPLIER
    print(f"Final score: {score}")


play_game()
