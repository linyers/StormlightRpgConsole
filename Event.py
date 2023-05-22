import abc
import typing

if typing.TYPE_CHECKING:
    from Game import Game

class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def visitGame(self, game:'Game'):
        pass