from enum import Enum

class Action(Enum):
	ATTACK = 1
	HEAL = 2
	QUIT = 3

	def description(self) -> str:
		if self == self.ATTACK:
			return "Attack monster"
		elif self == self.HEAL:
			return "Heal yourself"
		elif self == self.QUIT:
			return "Quit game"
		else:
			raise Exception("Not valid action!")

	def __str__(self) -> str:
		if self == self.ATTACK:
			return "a"
		elif self == self.HEAL:
			return "h"
		elif self == self.QUIT:
			return "q"
		else:
			raise Exception("Not valid action!")

	@classmethod
	def strToAction(cls, string) -> 'Action':
		if string == "a":
			return cls.ATTACK
		elif string == "h":
			return cls.HEAL
		elif string == "q":
			return cls.QUIT
		else:
			raise ValueError("action not valid")
