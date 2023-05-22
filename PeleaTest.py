import typing
from Soldier import Soldier
import Character

def takeDamageTest(enemy: 'Character'):
    soldier = Soldier()

    soldier.eventObserver.subscribe(
        lambda evento: print(evento)
    )

    for i in range(3):
        enemy.attack(soldier)

def tests():
    takeDamageTest(Soldier())