# SNAKES AND LADDERS

import random
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # so each new line defaults to white text

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


class Player:
    """
    Player class
    """

    def __init__(self, pawn_color, curr_position=0):
        # instance properties
        self.pawn_color = pawn_color
        self.curr_square = curr_position

    # instance methods
    def location(self):
        """
        return a statement representing this object's current position:
        (plan is to update the VALUE ingame with dice roll or landing on a \
        snake head/ladder foot to simulate player's current position)
        """
        player_location = {f"{self.pawn_color} pawn is on square \
        {self.curr_square} "}

        return player_location


def view_rules():
    '''
    Clear screen
    View Rules
    Back to welcome screen
    '''
    # print("View Rules TEST")  # testing
    # Use multiline comments as cleaner than using multiple print statements
    # and/or using Implicit concatenation to keep strings < 80 chars long
    # https://stackoverflow.com/a/1874679

    view_rules = """
    ==========================================================================

    HOW TO PLAY

    NEEDED:
    🎲 2-4 players
    🎲 1 six sided dice
    🎲 Pawns (1 color for each player) - Red, Green, Blue, Yellow
    🎲 Playing board

    FOR EACH PLAYER:
    🎲 Each player throws the dice and moves their pawn according to the
    number shown on the dice.
    🎲 If a player's pawn lands on an empty square there is no effect.
    🎲 If a player's pawn ends its move at the foot of a ladder, the pawn must
    move immediately to the square at the top of that ladder.
    🎲 If a player's pawn ends its move at the head of a snake, the pawn must
    immediately move to the square at the tail of that snake.

    TO WIN:
    🎲  Be the first player to reach or pass square 100.

    ==========================================================================
    """
    clear_terminal()
    print(view_rules)
    while True:
        try:
            # code to run regardless, it may throw an exception...
            go_back_choice = int(
                input(f"{Fore.RED}{Back.WHITE} 1 {Fore.WHITE}{Back.BLACK} Go back\n"))
            if not input:
                raise ValueError
            elif go_back_choice == 1:
                sleep()  # short time delay
                clear_terminal()  # clear terminal
                welcome_screen()  # go back to welcome screen

        except ValueError:
            # capture no input or text input
            sleep()
            print(f"{Fore.RED}No input or text entered.  Key 1 to return.\n")

        else:
            # tell user if out of range number entered
            sleep()
            print(f"{Fore.RED}Incorrect number keyed. Key 1 to return.\n")


def view_board():
    # print("View Board TEST")  # testing
    '''
    Clear Terminal
    Build a 10 * 10 board and
    (Display the board for the user after each dice roll)
    '''
    clear_terminal()

    # create board - is just a list of 10 nested lists.
    board = []
    # for i in range(0, 10):
    # the quick way
    # board.append(["⬜"]*10)
    # give each square a number
    # limitation in method. cannot display like proper board below
    # as working within nested list structures
    board.append(['📏', '02', '03', '📏', '05', '06', '07', '08', '📏', '10'])
    board.append(['11', '12', '13', '14', '15', '🐍', '17', '18', '19', '20'])
    board.append(['📏', '22', '23', '24', '25', '26', '27', '📏', '29', '30'])
    board.append(['31', '32', '33', '34', '35', '📏', '37', '38', '39', '40'])
    board.append(['41', '42', '43', '44', '45', '46', '47', '🐍', '49', '50'])
    board.append(['📏', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
    board.append(['61', '62', '63', '🐍', '65', '66', '67', '68', '69', '70'])
    board.append(['📏', '72', '73', '74', '75', '76', '77', '78', '79', '📏'])
    board.append(['81', '82', '83', '84', '85', '86', '87', '88', '89', '90'])
    board.append(['91', '92', '🐍', '94', '🐍', '96', '🐍', '🐍', '99', '🏁'])

    # REVIEW BOARD - WANT ONE MORE TRADITIONAL LOOKING

    # stack lists on top of each other & print
    for i in board:
        print(" ".join(i))  # use join method from list with one space in beautify board.
    while True:
        try:
            # code to run regardless, it may throw an exception...
            go_back_choice = int(
                input(f"{Fore.RED}{Back.WHITE}\n 1 {Fore.WHITE}{Back.BLACK} Go back\n"))
            if not input:
                raise ValueError
            elif go_back_choice == 1:
                clear_terminal()  # clear terminal
                welcome_screen()  # go back to welcome screen

        except ValueError:
            # capture no input or text input
            sleep()
            print(f"{Fore.RED}{Back.BLACK}No input or text entered.  Key 1 to return.\n")

        else:
            # tell user if out of range number entered
            sleep()
            print(f"{Fore.RED}{Back.BLACK}Incorrect number keyed. Key 1 to return.\n")


def game_setup():
    """
    Ask user for number of players between 2 - 4
    Call function to validate user input
    Apply pawn color to each player,
    P1 = red, P2 = green, P3 = blue, P4 = yellow
    """
    clear_terminal()

    while True:

        # Immediately convert string input from user to an integer
        # errorhandle both for an empty string and non int value
        # https://stackoverflow.com/a/4994509
        try:
            # code to run regardless, it may throw an exception...
            player_count = int(input(
                f"{Back.BLACK}Enter number of players between 2 and 4:\n"))
            if not input:
                raise ValueError

            if validate_player_count(player_count):
                print(f"{Fore.GREEN}{Back.BLACK}\nValid input. Creating players...\n")
                # create list of players - use pawn color
                player_list = []

                # loop - create a list of a unique for each player.
                for p in range(1, player_count + 1):
                    if p == 1:
                        player_list.append("Red")
                    elif p == 2:
                        player_list.append("Green")
                    elif p == 3:
                        player_list.append("Blue")
                    else:
                        player_list.append("Yellow")

                players = {pawn_color: Player(
                    pawn_color=pawn_color) for pawn_color in player_list}
                break

        except ValueError:
            # except - if an exception thrown, clear terminal and restart
            print(f"{Fore.RED}{Back.BLACK}\nNo value or text value submitted...\n")

    return snl_game(players)


def validate_player_count(player_count):
    """
    Check number of players supplied from game_setup() function
    is an integer >= 2 and <= 4
    """
    try:
        if player_count < 2 or player_count > 4:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}{Back.BLACK}You entered {player_count} player(s). Try again...\n")
        return False

    # return True if validation finds errors to ask user to re enter \
    # number of players to continue while loop
    return True


def snl_game(players):
    """
    Iterate players
    Loop through each until win condition met
    """
    while True:

        for player_id, player_inst in players.items():
            # key is the player iterable, value is the Player object instance
            # check if player rolled a six, repeat same iteration
            # https://stackoverflow.com/a/7293992
            # Default is True to get loop started for 1st iteration only

            print(f"Player '{player_id}' turn")
            # print(f"Confirming six_rolled '{player_inst.extra_roll}' for current player '{player_id}' on previous roll.")
            # establish current player's location on board and
            # assign the object attr to 'curr_position' using .notation
            curr_position = player_inst.curr_square
            print(f"Player '{player_id}' current location is square '{curr_position}'.")  # testing
            # now pass curr_position variable to turn() function to process
            # the players new location based off their next dice roll
            new_position = turn(player_id, player_inst, curr_position)
            # print(f"player '{player_id}' rolled a six value is '{player_inst.extra_roll}'.")
            # update player instance attr with returned value from turn()
            player_inst.curr_square = new_position  # testing
            print(f"Player '{player_id}' new location is square '{player_inst.curr_square}'.\n")  # testing

            # check if win condition met
            check_win(player_id, player_inst)


def roll_dice(player_inst):
    roll = random.randint(1, 6)
    return roll


def turn(player_id, player_inst, curr_position):
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
    roll_num = roll_dice(player_inst)
    new_position = curr_position + roll_num
    print(f"Player '{player_id}' rolled a '{roll_num}' and moves from square '{curr_position}' to square '{new_position}'.")
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


def check_win(player_id, player_inst):
    '''
    check if player has reached or passed 100
    if they have exit the program
    '''
    if player_inst.curr_square >= 100:
        print(f"Player '{player_id}' wins!\n")
        exit()


def welcome_screen():
    """
    1. Display title
    2. Options
    3. Ask user to begin game or quit application
    """
    # display title
    title = "SNAKES AND LADDERS\n"
    print(f"{Fore.GREEN}{Back.BLACK}{Style.BRIGHT}{title}")
    # Ask user to begin game or quit application

    print(f"{Back.BLACK}Select an option: \n")
    print(f"{Fore.RED}{Back.WHITE} 1 {Fore.WHITE}{Back.BLACK} View Rules    \n")
    print(f"{Fore.GREEN}{Back.WHITE} 2 {Fore.WHITE}{Back.BLACK} View Board    \n")
    print(f"{Fore.BLUE}{Back.WHITE} 3 {Fore.WHITE}{Back.BLACK} Play Game     \n")

    try:
        # code to run regardless, it may throw an exception...
        pre_game_choice = int(input(f"{Back.BLACK}Select from options {Fore.RED}{Back.BLACK}1{Fore.WHITE}, {Fore.GREEN}2 {Fore.WHITE}{Back.BLACK}or {Fore.BLUE}3{Fore.WHITE} \n"))
        if not input:
            raise ValueError
        elif pre_game_choice == 1:
            view_rules()
        elif pre_game_choice == 2:
            view_board()
        elif pre_game_choice == 3:
            game_setup()
        else:
            incorrect_value()

    except ValueError:
        # except - if exception thrown, clear terminal and restart application
        # capture nums out of range or text input
        print(f'{Fore.RED}{Back.BLACK}Oops! Incorrect value submitted.')
        sleep()  # short time delay
        clear_terminal()  # clear terminal
        pre_game()  # restart program


def incorrect_value():
    '''
    If value entered isn't a number from 1 to 3 throw an error
    '''
    print(f'{Fore.RED}{Back.BLACK}\nOops! Incorrect value submitted. Restarting application')
    clear_terminal()  # clear terminal
    pre_game()  # restart program


def clear_terminal():
    """
    clear the terminal.
    Credit Tim Nelson & [poke](https://stackoverflow.com/a/2084628)
    """
    sleep()
    os.system("cls" if os.name == "nt" else "clear")


def sleep():
    '''
    Display returned input for 2 seconds to be human readible
    '''
    time.sleep(1)


def pre_game():
    """
    Start of the program
    """
    welcome_screen()


pre_game()  # program start
