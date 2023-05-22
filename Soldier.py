from Sword import Sword
from Character import Character

class Soldier(Character):

    def __init__(self):
        super().__init__(5, Sword(), "Soldado")