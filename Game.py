import typing
from rx.subject import Subject

from Soldier import Soldier

if typing.TYPE_CHECKING:
    from Kaladin import Kaladin
    from Event import Event
    from Character import Character

class Game:
    def __init__(self, player:'Kaladin'):
        self.player = player
        self.actualEnemy: 'Character' = Soldier()
        self.listEnemy = [
            Soldier(),
            Soldier()
        ]

        self.playerDisposable = self.player.eventObserver.subscribe(self.acceptEvent) #pendiente
        self.actualEnemyDisposable = \
            self.actualEnemy.eventObserver.subscribe(self.acceptEvent) #pendiente

        self.result: Subject[bool] = Subject()
        self.nameSigEnemy: Subject[str] = Subject()

    def liberate(self) -> None:
        self.playerDisposable.dispose()
        self.actualEnemyDisposable.dispose()

    def win(self) -> None:
        self.liberate()
        self.result.on_next(True)
        self.result.on_completed()

    def lose(self) -> None:
        self.liberate()
        self.result.on_next(False)
        self.result.on_completed()
    
    def acceptEvent(self, event: 'Event') -> None:
        event.visitGame(self)

    def sigEnemy(self) -> None:
        self.actualEnemyDisposable.dispose()
        if len(self.listEnemy) == 0:
            self.win()
        else:
            self.actualEnemy = self.listEnemy.pop()
            self.actualEnemyDisposable = \
                self.actualEnemy.eventObserver.subscribe(self.acceptEvent)
            self.nameSigEnemy.on_next(self.actualEnemy)
    
    def interaction(self, attacker: 'Character', receiver: 'Character') -> str:
        attacker.attack(receiver)
        return "{} recibio daño".format(receiver.__str__())
    
    def playerAttack(self) -> str:
        return self.interaction(self.player, self.actualEnemy)
    
    def enemyAttack(self) -> str:
        return self.interaction(self.actualEnemy, self.player)
    
    def start(self) -> None:
        self.nameSigEnemy.on_next(self.actualEnemy)

    def actualEnemyStatus(self) -> bool:
        return self.actualEnemy.health != 0