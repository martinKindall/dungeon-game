import abc

from logic.weapon.Weapon import Weapon


class Fighter(metaclass=abc.ABCMeta):

	def __init__(
			self,
			name: str,
			maxHitpoints: int,
			hitpoints: int,
			weapon: Weapon,
			exp: int):

		self.name = name
		self.maxHitpoints = maxHitpoints
		self.hitpoints = hitpoints
		self.weapon = weapon
		self.exp = exp

	def getAttackPoints(self) -> int:
		return self.weapon.getAttackPoints()

	def receiveDamage(self, fighter: 'Fighter') -> None:
		self.hitpoints -= fighter.getAttackPoints()
		if self.hitpoints < 0:
			self.hitpoints = 0

	def attack(self, fighter: 'Fighter') -> None:
		fighter.receiveDamage(self)
