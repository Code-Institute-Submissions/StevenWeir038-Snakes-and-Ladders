# Use multiline comments as cleaner than using multiple print statements
# and/or using Implicit concatenation to keep strings < 80 chars long
# https://stackoverflow.com/a/1874679

def game_instructions():
    """
    separation of concern
    rules for view_rules() in run.py
    """
    VIEW_RULES = """
    🐍 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 🐍
    *                                                                       *
    * HOW TO PLAY                                                           *
    *                                                                       *
    * NEEDED:                                                               *
    * 🎲 2-4 players                                                        *
    * 🎲 1 six sided dice                                                   *
    * 🎲 Pawns (1 color for each player) - Red, Green, Blue, Yellow         *
    * 🎲 Playing board                                                      *
    *                                                                       *
    * FOR EACH PLAYER:                                                      *
    * 🎲 Each player throws the dice and moves their pawn according to the  *
    *    number shown on the dice.                                          *
    * 🎲 If a player's pawn lands on an empty square there is no effect.    *
    *                                                                       *
    * 🎲 If a player's pawn ends its move at the foot of a ladder, the pawn *
    *    must move immediately to the square at the top of that ladder.     *
    *                                                                       *
    * 🎲 If a player's pawn ends its move at the head of a snake,           *
    *    the pawn must immediately move to the square at the tail of that   *
    *    snake                                                              *
    *                                                                       *
    * TO WIN:                                                               *
    * 🎲  Be the first player to reach or pass square 100.                  *
    *                                                                       *
    🐍 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 🐍
    """

    return VIEW_RULES
