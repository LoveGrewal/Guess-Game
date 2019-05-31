# Guess-Game

Guess the word and have details analysis for the points won  

### Prerequisites and Running

What things you need to install the software and how to install them

```
1. Python 3.7.0
2. fourLetters.txt database which stores woed for guessing game.
3. frequency.txt table for letters which is used for points earned.
4. Command : guess.py
```

### Technical Details

```
Python 3.7.0
Guess.py : main logic to play game
stringDatabase : it loads the words from database at initialize and keep the words list in static variable
game.py : class to store objects of game details for player.
```

###Test Cases

It interacts with player with menu: 

```
g = guess, t = tell me, l for a letter, q to quit
```

It will print the table with number of games and the details for that game containing original word, status, bad guesses, missed letters and score. There will be final score by adding all the game score

###More Information

Refer A1.pdf for assignment details and marking criteria.
