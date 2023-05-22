from Weapons import Weapon

class Spear(Weapon):
    def getAttackPoints(self) -> int:
        return 3

    def __str__(self) -> str:
        return "Lanza"