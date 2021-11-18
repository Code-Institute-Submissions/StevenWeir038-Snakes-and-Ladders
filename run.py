import random
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # so each new line defaults to white text

"""
Create dictionary to simulate snake and ladder movements.
Ladder goes up, snake moves down.  Can be represented in the same
dictionary as they perform similar function.  Just invert the values.
"""
SNAKE_LADDER = {
  98: 78,
  97: 76,
  95: 24,
  93: 68,
  64: 60,
  48: 30,
  16: 6,
  1: 38,
  4: 14,
  9: 31,
  21: 42,
  28: 84,
  36: 44,
  51: 67,
  71: 91,
  80: 100
}


def game_instructions():
    """
    Print game requirements, rules and victory condition to console
    for player to view
    """
    # Use multiline comments as cleaner than using multiple print statements
    # and/or using Implicit concatenation to keep strings < 80 chars long
    # https://stackoverflow.com/a/1874679
    game_about = """
    GAME REQUIREMENTS
    - Number of players: 2-4
    - Required: 1 dice (six sided), pawns (1 for each player), playing board

    PRE-GAME
    - Each player takes a different color pawn and throws the dice.

    GAME RULES
    - The first player throws the dice and moves their pawn according to the
      number shown on the dice.
    - If a player's pawn lands on an empty square there is no effect.
    - If a player's pawn ends its move at the foot of a ladder, the pawn must
      move immediately to the square at the top of that ladder.
    - If a player's pawn ends it move at the head of a snake, the pawn must
      immediately move to the tail of that snake.
    - Each time a player throws a 6, they are entitled to roll the dice and
      move again.
    - (Additional rule) If a player's pawn lands on a square occupied by an
      opponents pawn, that pawn is removed from the board and they must start
      again.
    - (Additional Rule) An exact throw is required to reach square 100.
      If the throw exceeds 100 the player must move backwards.
      Watch out for the snakes!

    VICTORY CONDITIONS
    - Be the first player to land on square 100.
    """
    print(game_about)


class Player:
    """
    Player class
    """
    def __init__(self, pawn_color, curr_square):
        # instance properties
        self.pawn_color = pawn_color
        self.curr_square = curr_square

    # instance methods
    def location(self):
        """
        return a dictionary representing this object's instance containing:
        the players pawn color as the KEY
        the players current position as the VALUE
        (plan is to update the VALUE ingame with dice roll or landing on a \
        snake head/ladder foot to simulate player's current position)
        """

        # empty dictionary
        player_info = {f"{self.pawn_color}: {0}"}

        return player_info


def game_setup():
    """
    Ask user for number of players between 2 - 4
    Call function to validate user input
    Apply pawn color to each player,
    P1 = red, P2 = blue, P3 = yellow, P4 = green
    """
    while True:

        # Immediately convert string input from user to an integer
        player_count = int(input("Enter number of players between 2 and 4:\n"))

        if validate_player_count(player_count):
            print("Valid input. Let the game begin...")
            break

        return player_count


def validate_player_count(player_count):
    """
    Check number of players supplied from game_setup() function
    is an integer >= 2 and <= 4
    """
    try:
        if player_count < 2 or player_count > 4:
            raise ValueError
    except ValueError:
        print("Invalid input. Try again...\n")
        # return False to game_setup() if validation finds no error \
        # in data to end the while loop
        return False

    # return True if validation finds errors to ask user to reenter \
    # number of players to continue while loop
    return True


def roll_dice():
    roll = random.randint(1, 6)
    return roll


def turn(player_num):
    """
    For each player turn, they start on square 0:
    1. Simulate dice roll. \
    2. Move pawn based on value rolled. \
    3. Evaluate if pawn landed on ladder foot or snake head, \
       and move to other end.
    4. Check if pawn lands on square 100 to win.
    5. Check of player rolled a six, \
       if so give them another roll, \
       if not move to next player.
    """
    position = 18
    roll_val = roll_dice()
    new_position = position + roll_val
    print(
        f"Player {player_num} rolled a {roll_val}. \
        Moves from square {position} to {new_position}.")
    # print(player_num)  # testing - remove
    # print(roll_val)  # testing - remove
    # print(position)  # testing - remove
    # print(new_position)  # testing - remove

    # evaluate if pawn has landed on a special square. \
    # If so migrate from key to value in SL dict


def main():
    """
    Run all program functions
    """
    # game title
    title = pyfiglet.figlet_format("Snakes And Ladders", font="small")
    print(title)
    # provides the user the game instructions
    game_instructions()
    # Game setup returns validated number for players input by user
    # player_count = game_setup()
    # print(f"There are {players} players")  #testing - remove
    # print(type(players))  # testing - remove
    # still to do player loop. Direct value for now to test turn().
    # turn(player_count)


main()
