from Event import Event
import typing

if typing.TYPE_CHECKING:
    from Game import Game

class EnemyDie(Event):

    def visitGame(self, game:'Game'):
        game.sigEnemy()