# SNAKES AND LADDERS

import random
import os
import time
from rules import game_instructions
import colorama
from colorama import Fore
colorama.init(autoreset=True)  # defaults new line text = white
from pyfiglet import Figlet
from termcolor import colored


class Board():
    """
    Board class
    """
    def __init__(self):
        # build list of 100 items and convert from integer to string
        board = []
        row = []
        for square in range(100, 0, -1):
            row.append(str(square).zfill(3))
            # build 1 row of 10 squares at a time
            # in inner loop, use modulo to find 1st number divisible by 10 = 0
            if (square-1) % 10 == 0:
                board.append(row)
                # clearout row list to ready for next loop
                row = []
        # after 10 lists built, reverse order of every even row in inner loop
        for column in range(10):  # 10 cols on board as 100 / 10 = 10
            # inner loop reverses order of list
            # to approximate classic board layout
            if column % 2:
                board[column].reverse()

        # format for terminal output
        for square in board:
            print(" | ".join(square))

        return


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
        player_location = {f"{self.pawn_color} is on square \
        {self.curr_square} "}

        return player_location


SNAKE_HEAD = {
    98: 78, 97: 76, 95: 24, 93: 68, 64: 60, 48: 30, 16: 6
}

LADDER_FOOT = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100
}


def print_center(msg):
    """
    center content on console
    """
    # Joe Iddon https://stackoverflow.com/a/52138950
    print(' ' * ((os.get_terminal_size().columns - len(msg))//2) + msg)


def quit_application():
    """
    confirm if user still wants to quit application
    display message and exit app after a short time
    """
    clear_terminal()
    # confirm if user still wants to quit application
    ans = input("\nAre you sure you want to quit? Y/N\n")
    if ans.lower() in ["y", "yes"]:
        clear_terminal()
        msg = "Thanks for playing!"
        print_center(msg)
        sleep(3)
        clear_terminal()
        exit()

    elif ans.lower() in ["n", "no"]:
        clear_terminal()
        menu_screen()

    else:
        quit_application()


def menu_return():
    """
    back to main menu
    """
    input(f"\nPress{Fore.BLUE} Enter{Fore.WHITE} to return\n")
    clear_terminal()
    menu_screen()


def view_rules():
    '''
    clear terminal
    view Rules (import from rules.py)
    Back to welcome screen
    '''
    clear_terminal()
    print(game_instructions())
    menu_return()


def draw_board():
    """
    make board list of 10 nested lists
    returns: nested lists
    """
# build list of 100 items and convert from integer to string
    board = []
    row = []
    for square in range(100, 0, -1):
        row.append(str(square).zfill(3))
        # build 1 row of 10 squares at a time
        # in inner loop, use modulo to find first number divisible by 10 = 0
        if (square-1) % 10 == 0:
            board.append(row)
            # clearout row list to ready for next loop
            row = []
    # after 10 lists built, reverse order of every even row in inner loop
    for column in range(10):  # 10 cols on board as 100 / 10 = 10
        # inner loop reverses order of list
        # to approximate classic board layout
        if column % 2:
            board[column].reverse()

    return board


def turn_board(position, board):
    """
    if value player position integer > 100, format square 100
    convert player position from integer to string
    evaluate player position string by looping through board list items
    format the matching list value
    return: None
    """
    # TEST INSIDE TURN BOARD
    # print(f"TURN BOARD - Player is on square {position}")  # testing

    str_pos = str(position).zfill(3)
    # first check if player is on or beyond square 100 to display flag
    # on square 100
    if position >= 100:
        board[0][0] = " 🏁 "

    # Replace all occurrences of an element in a nested list
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if col == str_pos:
                board[x][y] = " 📌 "

    # board_xy = [" 📌 " for x, row in enumerate(board) for y, col in enumerate(row) if col == str_pos]

    # format for terminal output
    for square in board:
        print(" | ".join(square))


def view_board():
    """
    for use in the menu to show player the board output
    clear terminal
    draw board using Board class
    menu option to go back to welcome screen
    """
    clear_terminal()
    Board()
    menu_return()


def game_setup():
    """
    clear terminal
    ask user for number of players between 2 - 4 (with error handling)
    call function to validate user input
    apply pawn color to each player,
    P1 = red, P2 = green, P3 = blue, P4 = yellow
    return: 'players' dictionary to snl_game()
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
                print(f"{Fore.GREEN}\nValid input. Building game for {Fore.WHITE}{player_count}{Fore.GREEN} players...\n")
                sleep(4)
                clear_terminal()
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
    parameters: number of players (integer) from game_setup()
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


def turn_prompt():
    """
    breakpoint to stop game autorunning
    this function can set it to autorun with a time delay between turns ie 5 seconds...
    returns: ?
    """

    input(f"\n{Fore.BLUE}ROLL DICE{Fore.WHITE} for next player?\n")


def snl_game(players):
    """
    parameters: 'players' dictionary from game_setup()
    iterate player
    loop through each until win condition met
    return: None
    """
    while True:

        for player_id, player_inst in players.items():
            # key is the player iterable, value is the Player object instance
            turn_prompt()
            clear_terminal()
            print(f"\nTURN - '{player_id}'")

            # breakpoint - user intervention to roll dice

            # establish current player's location on board and
            # assign the object attr to 'curr_position' using .notation
            curr_position = player_inst.curr_square
            print(f"'{player_id}' is on square '{curr_position}'.")

            # now pass curr_position variable to turn() function to process
            # the players new location based off their next dice roll
            new_position = move(player_id, curr_position)

            # update player instance attribute with returned value from move()
            player_inst.curr_square = new_position  # testing
            print(f"'{player_id}' moves to square '{new_position}'.\n")

            # display player position on a board in the terminal
            turn_board(new_position, draw_board())

            # check if win condition met
            check_win(player_id, player_inst)


def roll_dice():
    """
    generate number 1-6 using imported randint function and save to variable
    return: roll_num in move()
    """
    roll = random.randint(1, 6)
    return roll


def move(player_id, curr_position):
    """
    parameters: 'player_ID' and 'curr_position'  from snl_game()
    For each player move:
    1. get roll value from roll_dice()
    2. move x squares based on roll value.
    3. evaluate if pawn landed on snake, read dict key move to dict value
    4. evaluate if pawn landed on ladder, read dict key move to dict value
    return: player_id and current position to snl_game()
    """
    roll_num = roll_dice()
    new_position = curr_position + roll_num
    print(f"'{player_id}' rolled a '{roll_num}'")

    if new_position in SNAKE_HEAD:
        new_position = SNAKE_HEAD[new_position]
        print(f"'{player_id}' landed on a 🐍")
    elif new_position in LADDER_FOOT:
        new_position = LADDER_FOOT[new_position]
        print(f"'{player_id}' landed on a 🖇️")
    return new_position


def check_win(player_id, player_inst):
    '''
    evaluate if player has reached or passed 100 to terminate program
    '''
    if player_inst.curr_square >= 100:
        print(f"\n🎉 🎈'{player_id}' wins! 🎈 🎉\n")
        print("GAME OVER. Return to main menu")
        menu_return()


def menu_screen():
    """
    Menu
    """
    print("MENU\n")
    print(f"{Fore.RED}1 {Fore.WHITE}View Rules\n")
    print(f"{Fore.GREEN}2 {Fore.WHITE}View Board\n")
    print(f"{Fore.BLUE}3 {Fore.WHITE}Play Game\n")
    print(f"{Fore.YELLOW}4 {Fore.WHITE}Quit Application\n")

    try:
        pre_game_choice = int(input(f"Select from options {Fore.RED}1{Fore.WHITE}, {Fore.GREEN}2{Fore.WHITE}, {Fore.BLUE}3{Fore.WHITE}, {Fore.YELLOW}4{Fore.WHITE}\n"))
        if not input:
            raise ValueError
        elif pre_game_choice == 1:
            view_rules()
        elif pre_game_choice == 2:
            view_board()
        elif pre_game_choice == 3:
            game_setup()
        elif pre_game_choice == 4:
            quit_application()

        else:
            incorrect_value()

    except ValueError:
        print(f'{Fore.RED}Incorrect value submitted.')
        sleep(2)
        clear_terminal()
        menu_screen()


def incorrect_value():
    '''
    If value entered isn't a number from 1 to 4 throw an error
    '''
    print(f'{Fore.RED}\nIncorrect value submitted.')
    sleep(2)
    clear_terminal()
    menu_screen()


def clear_terminal():
    """
    clear the terminal.
    return: None
    """
    # Credit Tim Nelson & [poke](https://stackoverflow.com/a/2084628)
    os.system("cls" if os.name == "nt" else "clear")


def sleep(secs):
    '''
    display returned input for defined number of seconds for information to
    be useful to user
    return: None
    '''
    time.sleep(secs)


def pre_game():
    """
    Start of the program
    display title
    ask user if they want to view menu screen
    return: None
    """
    clear_terminal()
    title = Figlet(font='small')
    print(colored(title.renderText("Snakes  & Ladders"), 'yellow'))
    input(f"\nPress{Fore.BLUE} Enter{Fore.WHITE}\n")
    clear_terminal()
    menu_screen()


pre_game()  # program start
