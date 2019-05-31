import sys

class StringDatabase():
    """
    A class used to read from database and provide guess words and frequencies

    ...

    Attributes
    ----------
    wordsList : list
        a list of guess words
    frequencesTable : map
        the frequencies of letters

    Methods
    -------
    getNextWordForGame(postition)
        return the word at position
    getFrequencyOfLetter(letter)
        returns frequency of a letter
    """
    wordsList =[]
    frequencesTable = {'a' : 8.17,'b' : 1.49,'c' : 2.78,'d' : 4.25,'e' : 12.70,'f' : 2.23,'g' : 2.02,'h' : 6.09,'i' : 6.97,'j' : 0.15,'k' : 0.77,'l' : 4.03,'m' : 2.41,'n' : 6.75,'o' : 7.51,'p' : 1.93,'q' : 0.10,'r' : 5.99,'s' : 6.33,'t' : 9.06,'u' : 2.76,'v' : 0.98,'w' : 2.36,'x' : 0.15,'y' : 1.97,'z' : 0.07}
    try:
        with open("four_letters.txt", "r") as file:
            for line in file:
                x = line.split()
                wordsList.extend(x)
    except IOError:
        print("Problem reading file")
        sys.exit()
    except EOFError:
        print('Why did you do an EOF on me?')
        sys.exit()

    @staticmethod
    def getNextWordForGame(postition):
        """return the word at position

        Parameters
        ----------
        position : int
            location of a string

        Returns:
            str: a word for guessing game
        """
        return StringDatabase.wordsList[postition]
    @staticmethod
    def getFrequencyOfLetter(letter):
        """returns frequency of a letter

        Parameters
        ----------
        position : str
            character

        Returns:
            float: frequency of a letter
        """
        return StringDatabase.frequencesTable[letter]