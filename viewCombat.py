import typing
import Utils

from Action import Action

if typing.TYPE_CHECKING:
    from Game import Game
    from Kaladin import Kaladin

class viewCombat:
    def __init__(self, game: 'Game', player: 'Kaladin', enemy: str):
        self.game = game
        self.player = player
        self.enemy = enemy

        self.fight()
    
    def fight(self) -> None:
        print(self.enemy, "ha aparecido\n")

        while self.game.actualEnemyStatus():
            print('{} esta atacando!'.format(self.enemy))
            print(self.game.enemyAttack())
            input("Presiona una tecla para continuar...")
            Utils.cleanScreen()
            self.playerTurn()
            input("Presiona una tecla para continuar...")
            Utils.cleanScreen()

    def playerTurn(self) -> None:
        print(self.player)
        self.displayMenu()
    
    def displayMenu(self) -> None:
        playerAction = self.enterAction()
        print('\n')

        if playerAction == Action.ATTACK:
            print(self.game.playerAttack())
        elif playerAction == Action.RECOVER:
            self.player.recover()
            print(self.player.name + ' se ha recuperado')
        elif playerAction == Action.QUIT:
            print(self.player.name + ' se ha rendido')
            print('\nLa muerte es mi vida\nla fuerza se convierte en mi debilidad\nel viaje ha terminado.')
            exit()

    def enterAction(self) -> 'Action':
        while True:
            actionList: typing.List[Action] = [action  for action in Action]
            for action in actionList:
                print(action, "): ", action.description())
            try:
                actionPlayer = Action.strToAction(input(' -> Ingresa una accion: '))
            except ValueError: 
                print('Accion invalida')
            else:
                return actionPlayer