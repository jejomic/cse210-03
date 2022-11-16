import random


class GameController:
    """
    Implements game rules
    """

    def __init__(self):
        # list of words to be guessed
        self.__words = ['shortbow', 'sword', 'catalyst', 'claymore', 'polearm']
        # sets the word
        self.__secretWord = random.choice(self.__words)
        # sets hint
        self.__hint = []

        for i in self.__secretWord:
            self.__hint.append('_')

        # used to update director if player is right or wrong
        self.__progressCounter = [1, 1]

        self.__gameWon = False

    # secret word getter for debugging purposes
    def _GetSecretWord(self):
        return self.__secretWord

    # arg char used by director to get input
    def _CheckAnswer(self, char):

        # ensures that character wasn't used already
        guessedAlready = False

        if char in self.__secretWord and char in self.__hint:
            guessedAlready = True

        while guessedAlready:
            return

        # player guessed correctly
        if char in self.__secretWord and char not in self.__hint:

            for i, h, s in zip(range(0, len(self.__hint)), self.__hint, self.__secretWord):
                if h == '_' and s == char:
                    self.__hint[i] = char
        # player was wrong
        else:
            self.__progressCounter[1] = self.__progressCounter[1] - 1

    # returns the hint
    def _ShowHint(self):
        return self.__hint

    # director uses this to track game status and if player still has parachute
    def _TrackProgress(self, player):

        # if player was wrong, reduce parachute
        if self.__progressCounter[0] > self.__progressCounter[1]:
            player._DamageParachute()

            # reset for next round
            self.__progressCounter = [1, 1]

        # check player's parachute condition
        if len(player._GetParachute()) < 1:
            player._UpdateBody(['  \ /  ', '  \|/  ', '   x   '])
            player._UpdateHp(False)

        self.__IsGuessed()

    # checks if word has been guessed already
    def __IsGuessed(self):
        hint = "".join(self.__hint)
        if hint == self.__secretWord:
            self.__gameWon = True

    # sets if game was already won
    def _GameUpdate(self):
        return self.__gameWon
