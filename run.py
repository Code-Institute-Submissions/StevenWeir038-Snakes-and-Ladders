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
    - Be the first player to reach square *100*.
    """
    print(game_about)


def game_setup():



def main():
    """
    Run all program functions
    """
    game_instructions()
    game_setup()

main()
