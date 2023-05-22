from enum import Enum

class Action(Enum):
    ATTACK = 1
    RECOVER = 2
    QUIT = 3

    @classmethod
    def strToAction(cls, string) -> 'Action':
        if string == 'a':
            return cls.ATTACK
        elif string == 'r':
            return cls.RECOVER
        elif string == 'q':
            return cls.QUIT
        else:
            raise ValueError(f'Accion invalida: {string}')
        
    def __str__(self) -> str:
        if self == self.ATTACK:
            return 'a'
        elif self == self.RECOVER:
            return 'r'
        elif self == self.QUIT:
            return 'q'
        
    def description(self) -> str:
        if self == self.ATTACK:
            return 'Atacar enemigo'
        elif self == self.RECOVER:
            return 'Recuperar vida (hay algo raro en el viento)'
        elif self == self.QUIT:
            return 'Salir del juego'
        
        