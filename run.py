import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # so each new line defaults to white text

"""
Create dictionary to simulate snake and ladder movements.
Ladder goes up, snake moves down.  Can be represented in the same
dictionary as they perform similar function.  Just invert the values.
UPDATE - As I want to test snake and ladder rules separately, it is better to
separate SNAKE_HEAD & LADDER_FOOT dictionaries.
"""
SNAKE_HEAD = {
    98: 78,
    97: 76,
    95: 24,
    93: 68,
    64: 60,
    48: 30,
    16: 6
}

LADDER_FOOT = {
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
    🎲 Number of players: 2-4
    🎲 Required: 1 dice (six sided), pawns (1 for each player), playing board

    PRE-GAME
    🎲 Each player takes a different color pawn and throws the dice.

    GAME RULES
    🎲 The first player throws the dice and moves their pawn according to the
    number shown on the dice.
    🎲 If a player's pawn lands on an empty square there is no effect.
    🎲 If a player's pawn ends its move at the foot of a ladder, the pawn must
    move immediately to the square at the top of that ladder.
    🎲 If a player's pawn ends its move at the head of a snake, the pawn must
    immediately move to the square at the tail of that snake.
    🎲 Each time a player throws a 6, they are entitled to roll the dice and
    move again.

    VICTORY CONDITIONS
    🎲  Be the first player to land on square 100.

    ==========================================================================
    """
    print(game_about)


class Player:
    """
    Player class
    """

    def __init__(self, pawn_color, curr_position=0):
        # instance properties
        self.pawn_color = pawn_color
        self.curr_square = curr_position
        self.extra_roll = False

    # instance methods
    def location(self):
        """
        return a statement representing this object's:
        (plan is to update the VALUE ingame with dice roll or landing on a \
        snake head/ladder foot to simulate player's current position)
        """
        player_location = {f"{self.pawn_color} pawn is on square \
        {self.curr_square} "}

        return player_location


def game_setup():
    """
    Ask user for number of players between 2 - 4
    Call function to validate user input
    Apply pawn color to each player,
    P1 = red, P2 = green, P3 = blue, P4 = yellow
    """
    while True:

        # Immediately convert string input from user to an integer
        player_count = int(input("Enter number of players between 2 and 4:\n"))

        if validate_player_count(player_count):
            print("\nValid input. Creating players...")
            # create list of players - use pawn color
            player_list = []

            # loop to create a list of a unique 'pawn_color' for each player.

            for p in range(1, player_count + 1):
                if p == 1:
                    print("player one")  # testing
                    player_list.append("P1 red")
                elif p == 2:
                    print("player two")  # testing
                    player_list.append("P2 green")
                elif p == 3:
                    print("player three")  # testing
                    player_list.append("P3 blue")
                else:
                    print("player four")  # testing
                    player_list.append("P4 yellow")
            print(player_list)
            """
            https://stackoverflow.com/a/17662224
            build dictionary by looping over the player_list.
            The KEY takes the iteration value in the list, in this case
            the players pawn color. The associated value for each key will
            be the instantiated Player class object.
            In game, each instances attributes/methods can be accessed
            using it's key.  For example: player_list['P1 red']
            """
            player_dict = {pawn_color: Player(
                pawn_color=pawn_color) for pawn_color in player_list}
            break
    return player_dict


def validate_player_count(player_count):
    """
    Check number of players supplied from game_setup() function
    is an integer >= 2 and <= 4
    """
    try:
        if player_count < 2 or player_count > 4:
            raise ValueError
    except ValueError:
        print(f"You entered {player_count} player(s). Try again...")
        # return False to game_setup() if validation finds no error \
        # in data to end the while loop
        return False

    # return True if validation finds errors to ask user to re enter \
    # number of players to continue while loop
    return True


def roll_dice(player_instance):
    roll = random.randint(1, 6)
    # ternary expression to evaluate True or False
    another_turn = True if roll == 6 else False
    # assign bool value of another_turn variable to player_instance attribute
    player_instance.extra_roll = another_turn
    return roll


def turn(player_id, player_instance, curr_position):
    """
    For each player turn:
    1. Simulate dice roll - move to roll_dice()
    2. Move pawn based on value rolled.
    3. Evaluate if pawn landed on ladder foot or snake head,
    and move to other end.
    4. Check if pawn lands on square 100 to win - move to snl_game()
    5. Check of player rolled a six - move to snl_game()
    if so give them another roll - move to snl_game()
    6. By default, move to next player.
    """
    roll_num = roll_dice(player_instance)
    new_position = curr_position + roll_num
    print(
        f"Player '{player_id}' rolled a '{roll_num}' and moves from square '{curr_position}' to square '{new_position}'.")
    # evaluate if pawn has landed on a special square.
    # If so player moves from key to value in Snake/Ladder dict,
    # reassign value for current player object instance curr_position attribute
    # if player position matches key in SNAKE_HEAD, its value becomes the
    # snake tail which equals the SNAKE_HEAD value
    if new_position in SNAKE_HEAD:
        new_position = SNAKE_HEAD[new_position]
        print(f"Player '{player_id}' landed on a SNAKE_HEAD and moves to square '{new_position}'.")
    elif new_position in LADDER_FOOT:
        new_position = LADDER_FOOT[new_position]
        print(f"Player '{player_id}' landed on a LADDER_FOOT and moves to square '{new_position}'.")
    return new_position


def check_win(player_id, player_instance):
    if player_instance.curr_square >= 100:
        print(f"Player '{player_id}' wins!\n")
        return True


def snl_game(players):
    """
    Iterate players, loop through each until win condition met
    """
    # infinite loop needed to keep game live until victory condition met
    while True:
    # for i in range(50):  # testing for 50 turns

        for player_id, player_instance in players.items():
            # key is the player iterable, value is the Player object instance
            # establish current player's location on board and
            # assign the object attribute to 'curr_position' using .notation
            curr_position = player_instance.curr_square
            print(f"Player '{player_id}' current location is square '{curr_position}'.")  # testing
            # now pass curr_position variable to turn() function to process
            # the players new location based off their next dice roll
            new_position = turn(player_id, player_instance, curr_position)
            print(f"player '{player_id}' rolled a six value is '{player_instance.extra_roll}'.")
            # update player instance attribute with returned value from turn()
            player_instance.curr_square = new_position  # testing
            print(f"Player '{player_id}' new location is square '{player_instance.curr_square}'.\n")  # testing

            # check if win condition met
            winner = check_win(player_id, player_instance)
            if winner:
                exit()
            else:
                # repeat same iteration - https://stackoverflow.com/a/7293992
                # check if player rolled a six.  Default is False,
                extra_roll = player_instance.extra_roll
                if extra_roll is True:
                    curr_position = player_instance.curr_square
                    print(f"Player '{player_id}' current location is square '{curr_position}'.")  # testing
                    new_position = turn(player_id, player_instance, curr_position)
                    print(f"player '{player_id}' rolled a six value is '{player_instance.extra_roll}'.")
                    player_instance.curr_square = new_position  # testing
                    print(f"Player '{player_id}' new location is square '{player_instance.curr_square}'.\n")  # testing
                    # check if win condition met
                    winner = check_win(player_id, player_instance)
                    if winner:
                        exit()


def main():
    """
    Run all program functions
    """
    # game title
    title = "SNAKES ANDS LADDERS"
    print(f"{Fore.GREEN}{title}")
    # provides the user the game instructions
    game_instructions()
    # game setup returns validated number for players input by user
    players = game_setup()  # players = dict of players rtnd from game_setup()
    print(f"{players}\n")  # testing - shows diff memory allocation for each instance
    snl_game(players)  # pass 'players' dictionary to the game


main()
