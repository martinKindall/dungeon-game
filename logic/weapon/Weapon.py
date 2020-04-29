import abc

class Weapon(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def getAttackPoints(self) -> int:
		pass

	@abc.abstractmethod
	def __str__(self) -> str:
		pass
