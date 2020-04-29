from logic.weapon.Weapon import Weapon


class Club(Weapon):

	def getAttackPoints(self) -> int:
		return 2

	def __str__(self) -> str:
		return "Club"
