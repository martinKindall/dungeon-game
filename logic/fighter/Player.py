from logic.fighter.Fighter import Fighter
from logic.weapon.Sword import Sword


class Player(Fighter):

	def __init__(self):
		super().__init__("Jugador", 10, Sword(), 0)

	def selfHeal(self) -> None:
		self.hitpoints += 3
