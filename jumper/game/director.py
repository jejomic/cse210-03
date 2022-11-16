from game.gamecontroller import GameController
from game.terminalservice import TerminalService
from game.parachuteguy import ParachuteGuy
import random


class Director:
    """
    directs the game
    """

    def __init__(self):

        self._terminalService = TerminalService()
        self._parachuteGuy = ParachuteGuy()
        self._gameController = GameController()

    def __GetInputs(self):
        playerAnswer = ''
        while True:
            playerAnswer = self._terminalService._ReadText(
                "\nGuess a letter [a-z]: ")
            if len(playerAnswer) == 1:
                break
            else:
                self._terminalService._DisplayText(
                    "Enter a single character only")
                continue

        self._gameController._CheckAnswer(playerAnswer)

    def __DoUpdates(self):
        self._gameController._TrackProgress(self._parachuteGuy)

    def __DoOutputs(self):
        self._terminalService._DisplayText("\n")
        self._terminalService._ListToText(self._gameController._ShowHint())
        self._terminalService._DisplayText("\n")
        self._terminalService._DisplayObject(
            self._parachuteGuy._GetParachute())
        self._terminalService._DisplayObject(self._parachuteGuy._GetBody())
        self._terminalService._DisplayText("\n^^^^^^^")

    def StartGame(self):
        self._terminalService._ListToText(self._gameController._ShowHint())
        while self._parachuteGuy._CheckHp():
            if self._gameController._GameUpdate():
                self._terminalService._DisplayText("Congratulations! You won the game!")
                break
            self.__GetInputs()
            self.__DoUpdates()
            self.__DoOutputs()

        if not self._parachuteGuy._CheckHp():
            self._terminalService._DisplayText("You fell")
