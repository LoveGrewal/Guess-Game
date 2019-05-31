from random import randint
from game import Game
from stringDatabase import StringDatabase


class Guess():
    """
    A class used to start the guessing game (max guess word 100)
    ...

    Attributes
    ----------
    mainMenu : str
        display options for main menu
    successStatus : str
        the success status(to be stored for each game)
    failureStatus : str
        the failure status

    Methods
    -------
    checkGuess(game)
        check whether the guess is correct or not
    tellAnswer(game)
        tells the solution of a game
    checkLetter(game)
        check if the letter is present in guess word or not
    calculateScore(game)
        display the detail score for the whole guessing game
    startGuessGame(totalNumberOfGuessGames)
        start the guessing game
    """
    mainMenu = 'g = guess, t = tell me, l for a letter, q to quit'
    successStatus = 'success'
    failureStatus = 'gave up'
    
    def checkGuess(self, game):
        """check whether the guess is correct or not

        It will also calculate score for a current game (only including unguessed letters)

        Parameters
        ----------
        game : Game
            object of a current game

        Returns:
            boolean: if guessed correctly
        """
        actualGuessWord = list(game.word)
        guessWord = input("Enter your guess: ")
        if(guessWord.lower() == game.word):
            print("Correct guess")
            print('word - ' + game.word)
            #scoring
            score = 0
            for l in [i for i, letter in enumerate(game.progressWord) if letter == '-']:
                score = score + StringDatabase.getFrequencyOfLetter(actualGuessWord[l])
            if(game.missedLetters > 0):
                score = score / game.missedLetters
                
            game.score = game.score + score
            return True
        else:
            print('Wrong guess')
            game.badGuesses = game.badGuesses + 1
            #scoring
            score = 0
            for l in [i for i, letter in enumerate(game.progressWord) if letter == '-']:
                score = score + StringDatabase.getFrequencyOfLetter(actualGuessWord[l])
            score = score * 0.10
            game.score = game.score - score
            return False
    
    def tellAnswer(self, game):
        """tells the solution of a game

        It will also calculate score for a current game (with penalty for telling the solution)

        Parameters
        ----------
        game : Game
            object of a current game
        """
        actualGuessWord = list(game.word)
        #scoring
        score = 0
        for l in [i for i, letter in enumerate(game.progressWord) if letter == '-']:
            score = score + StringDatabase.getFrequencyOfLetter(actualGuessWord[l])
        game.score = game.score - score
        print('The answer is : ' + game.word)

    def checkLetter(self, game):
        """check if the letter is present in guess word or not

        It will also calculate score for a current game (only including unguessed letters)

        Parameters
        ----------
        game : Game
            object of a current game

        Returns:
            boolean: if guessed correctly
        """
        guessLetter = input("Enter your a letter: ")
        currentGuessWord = list(game.progressWord)
        if(guessLetter in game.word):
            occurence = 0
            for l in [i for i, letter in enumerate(game.word) if letter == guessLetter]:
                currentGuessWord[l] = guessLetter
                occurence = occurence + 1
            game.progressWord = ''.join(currentGuessWord)
            print('Letter found - ' + str(occurence))
            if('-' in game.progressWord):
                return False
            else:
                print('you found all letters in word - ' + game.progressWord)
                return True
        else:
            print('Wrong letter guess')
            game.missedLetters = game.missedLetters + 1

        return False
    
    def calculateScore(self, game):
        """display the detail score for the whole guessing game

        Parameters
        ----------
        game : Game
            object of a current game
        """
        idx = []
        words = []
        status = []
        badGuesses = []
        missedLetters = []
        score = []
        titles = ['game', 'word', 'status', 'bad guesses', 'missed letters', 'score']
        finalScore = 0

        i = 1
        for g in game:
            if(g.attempted):
                idx.append(i)
                words.append(g.word)
                status.append(g.status)
                badGuesses.append(g.badGuesses)
                missedLetters.append(g.missedLetters)
                score.append(round(g.score, 2))
                finalScore = finalScore + round(g.score, 2)
                i = i + 1
        data = [titles] + list(zip(idx, words, status, badGuesses, missedLetters, score))
        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(15) for x in d)
            print(line)
            if(i == 0):
                print('-' * len(line))
        print()
        print('Final Score : ' + str(round(finalScore, 2)))

            

    def startGuessGame(self, totalNumberOfGuessGames):
        """start the guessing game

        provides the menu and skeleton for guessing game and call appropriate method when needed

        Parameters
        ----------
        totalNumberOfGuessGames : int
            maximum number of time game can be played
        """
        i=0
        gameList = []
        print('The Guessing Game')
        while (i<totalNumberOfGuessGames):
            choice = ''
            #generate random number
            randomNumber = randint(0, len(StringDatabase.wordsList))
            #initialize current game object
            g = Game(StringDatabase.getNextWordForGame(randomNumber), '', 0, 0, 0, '----', False)
            #skeleton logic
            while(True):
                choice = ''
                print()
                print('curent Guess : ' + g.progressWord)
                print()
                print(Guess.mainMenu)
                choice = input("Enter your choice: ")
                
                if(choice.lower() == 'g'):
                    g.attempted = True
                    if(self.checkGuess(g)):
                        g.status = Guess.successStatus
                        break
                elif(choice.lower() == 't'):
                    g.attempted = True
                    g.status = Guess.failureStatus
                    self.tellAnswer(g)
                    break
                elif(choice.lower() == 'l'):
                    g.attempted = True
                    if(self.checkLetter(g)):
                        g.status = Guess.successStatus
                        break
                elif(choice.lower() == 'q'):
                    actualGuessWord = list(g.word)
                    #scoring
                    if(g.attempted):
                        score = 0
                        for l in [i for i, letter in enumerate(g.progressWord) if letter == '-']:
                            score = score + StringDatabase.getFrequencyOfLetter(actualGuessWord[l])
                        g.score = g.score - score
                    g.status = Guess.failureStatus
                    break
                
            gameList.append(g)
            i = i+1
            if(choice.lower() == 'q'):
                break

        self.calculateScore(gameList)

if __name__ == "__main__":
    g = Guess()
    totalNumberOfGuessGames = 100
    g.startGuessGame(totalNumberOfGuessGames)
