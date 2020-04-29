from logic.events.PlayerDies import PlayerDies
from logic.fighter.Fighter import Fighter
from logic.weapon.Sword import Sword


class Player(Fighter):

	def __init__(self, name: str):
		super().__init__(name, 10, Sword(), 0)

	def selfHeal(self) -> None:
		self.hitpoints += 3

	def die(self) -> None:
		self.eventObservable.on_next(PlayerDies())
		self.eventObservable.on_completed()
