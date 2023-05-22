import abc
import typing
from rx.subject import Subject
import EnemyDie

if typing.TYPE_CHECKING:
    from Weapons import Weapon
    from Event import Event

class Character(metaclass=abc.ABCMeta):

    def __init__(self, maxHealth: int, weapon: 'Weapon', name: str):
        self.maxHealth = maxHealth
        self.weapon = weapon
        self.name = name
        self.health = self.maxHealth
        self.eventObserver: Subject['Event'] = Subject()

    def getAttackPoints(self) -> int:
        return self.weapon.getAttackPoints()
    
    def takeDamage(self, character: 'Character') -> int:
        self.health -= character.getAttackPoints()
        if self.health < 0:
            self.health = 0
            self.die()


    def attack(self, character: 'Character') -> int:
        character.takeDamage(self)

    def die(self) -> None:
        self.eventObserver.on_next(EnemyDie.EnemyDie())
        self.eventObserver.on_completed()

    def __str__(self) -> str:
        return self.name + ' con una ' + self.weapon.__str__() + ' HP: ' + str(self.health)