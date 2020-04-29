from enum import Enum

class Action(Enum):
	ATTACK = 1
	HEAL = 2
	EXIT = 3

	def description(self) -> str:
		if self.value == self.ATTACK:
			return "Attack monster"
		elif self.value == self.HEAL:
			return "Heal yourself"
		elif self.value == self.EXIT:
			return "Quit game"
		else:
			raise Exception("Not valid action!")

	def __str__(self) -> str:
		if self.value == self.ATTACK:
			return "a"
		elif self.value == self.HEAL:
			return "h"
		elif self.value == self.EXIT:
			return "q"
		else:
			raise Exception("Not valid action!")
