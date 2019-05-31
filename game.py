class Game(object):
    """
    A class is will store single game data
    """
    def __init__(self, word, status, badGuesses, missedLetters, score, progressWord, attempted):
        """
        Parameters
        ----------
        word : str
            The string for guessing game
        status : str
            The game status
        badGuesses : int
            count to store bad guesses
        missedLetters : int
            count to store missed letter
        score : float
            The score of a current game
        progressWord : str
            The guess word for a current progress
        attempted : boolean
            True if game is attempted by player
        """
        self.word = word
        self.status = status
        self.badGuesses = badGuesses
        self.missedLetters = missedLetters
        self.score = score
        self.progressWord = progressWord
        self.attempted = attempted