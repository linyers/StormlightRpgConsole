import abc

class Weapon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getAttackPoints(self) -> int:
        pass

    def __str__(self) -> str:
        pass