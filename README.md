# **Snakes and Ladders**
![Image of game board](docs/readme/game-image.png "Image of game board") 

Welcome to **Snakes and Ladders**, a classic boardgame enjoyed by children and adults throughout the world.

It's a game of simple logic and chance, therefore is well suited to being a first application to develop when learning Python. 

I do hope you enjoy this take on the original.

## Wireframes
The game's logic was mapped out before coding began using a free version of [Lucidchart](https://www.lucidchart.com/pages/).

This web based platform is intuitive to use due to it's drag, drop and snap capabilities.

![Mockup](docs/wireframes/flowchart.png "Game logic flowchart") 

## Future Adaptations
Three additional game rules can be applied for extra complexity.

1. Each time a player throws a 6, they are entitled to roll the dice and move again.
2. If a player's pawn lands on a square occupied by an opponents pawn, that pawn is removed from the board and they must start again. 
3. An exact throw is required to reach square 100.  If the throw exceeds 100 the player must move backwards. Watch out for the snakes!

## Deployment
[Go to DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions to deploy application to Heroku.

## Testing
Go to [TESTING.md](TESTING.md) to view known bugs and fixes.

## Technologies Used
Flowcharts created with [Lucidchart](https://www.lucidchart.com/pages/).

Web deployment with [*Heroku*](https://www.heroku.com/about)

Python version 3.8

Additional Python libraries used:
- **os** to clear terminal window
- **time** to produce time delays to user inputs
- **random** to simulate dice roll
- **colorama** to beautify display

## Media and Content
REVIEW
### Credits
Thank you to my mentor [Tim Nelson](https://tim.2bn.dev/) for his candor.  Fantastic as always.

Beyond the Code Institute LMS a few key sources cemented my understanding of how to combine working with loops, dictionaries and classes. In particular, accessing their attributes and using them within loops, lists and dictionary comprehensions.

- [Abarneret](https://stackoverflow.com/a/17662224)
- [Jobel](https://stackoverflow.com/a/41720350)
- [James Gallagher](https://careerkarma.com/blog/python-convert-list-to-dictionary/)
- [schneebuzz](https://stackoverflow.com/a/59999615)

To repeat the same iteration of a loop depending on a condition.
- [David Heffernan](https://stackoverflow.com/a/7293992)

Error handling for empty and non integer values at the same time.
- [Joshua Burns](https://stackoverflow.com/a/4994509)

To clear the terminal window
- [poke](https://stackoverflow.com/a/2084628)

To display a more traditional game board layout
- [Manish V. Panchmatia](https://stackoverflow.com/a/55241525)

### Content
[Emojis](https://emojipedia.org/) from emojipedia.

[Board image](https://www.istockphoto.com/vector/snakes-and-ladders-black-and-white-gm1066160462-285104267 "Board image") courtesy of iStock.

Browser background from [Wallpaper Cave](https://wallpapercave.com/w/wp9142232).

[SNAKE_HEAD and LADDER_FOOT dictionaries ](docs/readme/own-gameboard.png "Own Gameboard") based of a game purchased from [Ambassador Games](http://www.ambassadorgames.com/craftsman-deluxe-game-house.htm).
