from Weapons import Weapon

class Sword(Weapon):
    def getAttackPoints(self) -> int:
        return 3

    def __str__(self) -> str:
        return "Espada"