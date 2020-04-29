import abc
import typing
from rx.subject import Subject

from logic.events.MonsterDies import MonsterDies

if typing.TYPE_CHECKING:
	from logic.weapon.Weapon import Weapon
	from logic.events.Event import Event

class Fighter(metaclass=abc.ABCMeta):

	def __init__(
			self,
			name: str,
			maxHitpoints: int,
			weapon: 'Weapon',
			exp: int):

		self.name = name
		self.maxHitpoints = maxHitpoints
		self.hitpoints = maxHitpoints
		self.weapon = weapon
		self.exp = exp
		self.eventObservable: Subject['Event'] = Subject()

	def getAttackPoints(self) -> int:
		return self.weapon.getAttackPoints()

	def receiveDamage(self, fighter: 'Fighter') -> None:
		self.hitpoints -= fighter.getAttackPoints()
		if self.hitpoints <= 0:
			self.hitpoints = 0
			self.die()

	def attack(self, fighter: 'Fighter') -> None:
		fighter.receiveDamage(self)

	def die(self) -> None:
		self.eventObservable.on_next(MonsterDies())
		self.eventObservable.on_completed()

	def isDead(self) -> bool:
		return self.hitpoints < 1

	def __str__(self) -> str:
		return self.name + " with a " + self.weapon.__str__()
