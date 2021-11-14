import random

"""
Module docstring goes here
"""


def game_instructions():
  """
  Print game requirements, rules and victory condition to console
  for player to view
  """
  # Use multiline comments as cleaner than using multiple print statements
  # and/or using Implicit concatenation to keep strings < 80 chars long
  # https://stackoverflow.com/questions/1874592/how-to-write-very-long-string-that-conforms-with-pep8-and-prevent-e501
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
  - (Additional Rule) An exact throw is required to reach square 100.  If
    the throw exceeds 100 the player must move backwards.
    Watch out for the snakes!

  VICTORY CONDITIONS
  - Be the first player to land on square 100.
  """
  print(game_about)


def game_setup():
  """
  Ask user for number of players between 2 - 4
  Call function to validate user input
  Randomly apply pawn color to each player
  """
  while True:

    # Immediately convert string input from user to an integer
    players = int(input("Enter number of players between 2 and 4:\n"))

    if validate_player_count(players):
      print("Valid input. Let the game begin...")
      break

  return players


def validate_player_count(player_count):
  """
  Check number of players supplied from game_setup() function
  is an integer >= 2 and <= 4
  """
  try:
    if player_count < 2 or player_count > 4:
      raise ValueError
  except ValueError as error:
    print(f"Invalid input. Try again...\n")
    # return False to game_setup() if validation finds no error in data to end the while loop 
    return False

  # return True if validation finds errors to ask user to reenter number of players to continue while loop
  return True


def turn(player_num):
  """
  For each player turn, they start on square 0: 
  1. simulate dice roll, 2. move pawn based on value rolled, 3. evaluate if pawn landed on
  ladder foot or snake head and move to other end, 4. check if pawn lands on
  square 100 to win, 5. Check of player rolled a six, if so give them another roll,
  if not move to next player. 
  """
  position = 18
  roll_val = random.randint(1, 6)
  new_position = position + roll_val
  print(position)
  print(roll_val)
  print(new_position)


def main():
  """
  Run all program functions
  """
  # provides the user the game instructions
  game_instructions()
  # Game setup returns validated number for players input by user
  players = game_setup()
  # print(f"There are {players} players")  #testing - remove
  # print(type(players))  # testing - remove
  turn(1) # still to do player iteration loop. Direct value for now to test turn().


# main()  # uncomment after turn() is coded.
turn(1)