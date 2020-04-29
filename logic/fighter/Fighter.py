import abc

from rx.subject import Subject

from logic.events.Event import Event
from logic.weapon.Weapon import Weapon


class Fighter(metaclass=abc.ABCMeta):

	def __init__(
			self,
			name: str,
			maxHitpoints: int,
			weapon: Weapon,
			exp: int):

		self.name = name
		self.maxHitpoints = maxHitpoints
		self.hitpoints = maxHitpoints
		self.weapon = weapon
		self.exp = exp
		self.eventObservable: Subject[Event] = Subject()

	def getAttackPoints(self) -> int:
		return self.weapon.getAttackPoints()

	def receiveDamage(self, fighter: 'Fighter') -> None:
		self.hitpoints -= fighter.getAttackPoints()
		if self.hitpoints < 0:
			self.hitpoints = 0

	def attack(self, fighter: 'Fighter') -> None:
		fighter.receiveDamage(self)
