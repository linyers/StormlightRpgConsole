from Game import Game
from Kaladin import Kaladin
import Utils
from viewCombat import viewCombat

class Main:

    def __init__(self):
        self.player: 'Kaladin' = Kaladin()
        self.game = Game(self.player)

    def comenzar(self) -> None:
        self.startCombatView()
        self.startWinOrLossView()
        self.game.start()
    
    def startCombatView(self) -> None:
        self.game.nameSigEnemy.subscribe(
            lambda sigEnemy: self.cleanScreenAndViewEnemy(sigEnemy)
        )

    def cleanScreenAndViewEnemy(self, sigEnemy: str) -> None:
        Utils.cleanScreen()
        viewCombat(self.game, self.player, sigEnemy)
    
    def startWinOrLossView(self) -> None:
        self.game.result.subscribe(lambda hisWins: self.winner() if hisWins else self.loser())

    def winner(self) -> None:
        print("Ganaste!")
        print("Vida antes que Muerte\nFuerza antes que Debilidad\nViaje antes que Destino")
        exit()

    def loser(self) -> None:
        print("Perdiste...")
        exit()

if __name__ == '__main__':
    print('*-----------------------------------------------------------------*')
    print("*                   Bienvenid@ a Stormbless Game                  *")
    print('*                                                                 *')
    print('*                                                                 *')
    print('*             Basado en hechos del Camino de los Reyes            *')
    print('*   Preparate para encarnar un Kaladin en el ejercito de Amaram   *')
    print('*-----------------------------------------------------------------*')
    Main().comenzar()