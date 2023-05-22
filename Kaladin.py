from Spear import Spear
from Character import Character
from PlayerDie import PlayerDie

class Kaladin(Character):

    def __init__(self):
        super().__init__(20, Spear(), "Kaladin")

    def recover(self) -> None:
        self.health += 4
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def die(self) -> None:
        self.eventObserver.on_next(PlayerDie())
        self.eventObserver.on_completed()