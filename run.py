# SNAKES AND LADDERS

import random
import os
import time
from rules import game_instructions
import colorama
from colorama import Fore
colorama.init(autoreset=True)  # so each new line defaults to white text


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


SNAKE_HEAD = {
    98: 78, 97: 76, 95: 24, 93: 68, 64: 60, 48: 30, 16: 6
}

LADDER_FOOT = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}


def view_rules():
    '''
    Clear terminal
    View Rules (import from rules.py)
    Back to welcome screen
    '''
    clear_terminal()
    print(game_instructions())
    while True:
        try:
            # code to run regardless, it may throw an exception...
            go_back_choice = int(
                input(f"{Fore.RED}1 {Fore.WHITE}Go back\n"))
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


def draw_board():
    '''
    draw a board with classic layout
    '''
    # Credit to Manish V. Panchmatia(https://stackoverflow.com/a/55241525)
    for i in range(99, -1, -1):
        if (i // 10) % 2 == 0:
            print("{0:4d}".format(i - 10 + 2 * (10 - (i % 10))), end=" ")
        else:
            print("{0:4d}".format(i + 1), end=" ")
        if i % 10 == 0:
            print("\r")


def turn_board(position, board):
    """

    return:
    """
    print(f"Player is on square {position}")  # testing
    # print(board)  # testing


def view_board():
    """
    for use in the menu to show player the board output
    clear terminal
    draw board
    menu option to go back to welcome screen
    """
    clear_terminal()
    draw_board()

    while True:
        try:
            # code to run regardless, it may throw an exception...
            go_back_choice = int(
                input(f"{Fore.RED}\n1 {Fore.WHITE}Go back\n"))
            if not input:
                raise ValueError
            elif go_back_choice == 1:
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


def game_setup():
    """
    clear terminal
    ask user for number of players between 2 - 4 (with error handling)
    call function to validate user input
    apply pawn color to each player,
    P1 = red, P2 = green, P3 = blue, P4 = yellow
    return: dictionary of players to snl_game()
    """
    clear_terminal()

    while True:

        # Immediately convert string input from user to an integer
        # error handle both for an empty string and non int value
        # https://stackoverflow.com/a/4994509
        try:
            player_count = int(input(
                "Enter number of players between 2 and 4:\n"))
            if not input:
                raise ValueError

            if validate_player_count(player_count):
                print(f"{Fore.GREEN}\nValid input. Creating players...\n")
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
            print(f"{Fore.RED}\nNo value or text value submitted...\n")

    return snl_game(players)


def validate_player_count(player_count):
    """
    check the players list passed from game_setup()
    is an integer >= 2 and <= 4
    return: True / False to game_setup()
    """
    try:
        if player_count < 2 or player_count > 4:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}You entered {player_count} player(s). Try again.\n")
        return False

    return True


def snl_game(players):
    """
    iterate players
    loop through each until win condition met
    """
    while True:

        for player_id, player_inst in players.items():
            # key is the player iterable, value is the Player object instance

            print(f"\nTURN - '{player_id}'")

            # establish current player's location on board and
            # assign the object attr to 'curr_position' using .notation
            curr_position = player_inst.curr_square
            print(f"'{player_id}' is on square '{curr_position}'.")  # testing

            # now pass curr_position variable to turn() function to process
            # the players new location based off their next dice roll
            new_position = turn(player_id, curr_position)

            # update player instance attr with returned value from turn()
            player_inst.curr_square = new_position  # testing
            print(f"'{player_id}' moves to square '{player_inst.curr_square}'.\n")  # testing

            # display player position on board
            turn_board(new_position, draw_board())

            # check if win condition met
            check_win(player_id, player_inst)


def roll_dice():
    """
    generate number from 1-6 using imported randint function
    and save in a variable
    return: roll to turn()
    """
    roll = random.randint(1, 6)
    return roll


def turn(player_id, curr_position):
    """
    For each player turn:
    1. get roll value from roll_dice()
    2. move x squares based on roll value.
    3. evaluate if pawn landed on snake, read dict key move to dict value
    4. evaluate if pawn landed on ladder, read dict key move to dict value
    return: player_id and current position to snl_game()
    """
    roll_num = roll_dice()
    new_position = curr_position + roll_num
    print(f"'{player_id}' rolled a '{roll_num}'")
    # evaluate if pawn has landed on a special square.
    # If so player moves from key to value in Snake/Ladder dict,
    # reassign value for current player object instance curr_position attribute
    # if player position matches key in SNAKE_HEAD, its value becomes the
    # snake tail which equals the SNAKE_HEAD value
    if new_position in SNAKE_HEAD:
        new_position = SNAKE_HEAD[new_position]
        print(f"'{player_id}' landed on a 🐍")
    elif new_position in LADDER_FOOT:
        new_position = LADDER_FOOT[new_position]
        print(f"'{player_id}' landed on a 🖇️")
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
    title = "SNAKES AND LADDERS\n"
    print(f"{Fore.GREEN}{title}")

    print("MENU\n")
    print(f"{Fore.RED}1 {Fore.WHITE}View Rules\n")
    print(f"{Fore.GREEN}2 {Fore.WHITE}View Board\n")
    print(f"{Fore.BLUE}3 {Fore.WHITE}Play Game\n")

    try:
        pre_game_choice = int(input(
            f"Select from options {Fore.RED}1{Fore.WHITE}, {Fore.GREEN}2{Fore.WHITE} or {Fore.BLUE}3{Fore.WHITE}\n"))
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
        print(f'{Fore.RED}Incorrect value submitted.')
        sleep()
        clear_terminal()
        pre_game()


def incorrect_value():
    '''
    If value entered isn't a number from 1 to 3 throw an error
    '''
    print(f'{Fore.RED}\nIncorrect value submitted. Restarting application')
    clear_terminal()
    pre_game()


def clear_terminal():
    """
    clear the terminal.
    return: None
    """
    # Credit Tim Nelson & [poke](https://stackoverflow.com/a/2084628)
    sleep()
    os.system("cls" if os.name == "nt" else "clear")


def sleep():
    '''
    display returned input for 2 seconds to be human readible
    return: None
    '''
    time.sleep(1)


def pre_game():
    """
    Start of the program
    return: None
    """
    welcome_screen()


pre_game()  # program start
