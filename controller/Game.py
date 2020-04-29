from typing import List

from rx.subject import Subject

from logic.fighter.Fighter import Fighter
from logic.fighter.Goblin import Goblin
from logic.fighter.Player import Player


class Game:

	def __init__(self, player: Player):
		self.player = player
		self.gameResult: Subject[bool] = Subject()
		self.nextFighter: Subject[Fighter] = Subject()

		self.currentMonster: Fighter = Goblin()
		self.monsters: List[Fighter] = list()
		self.monsters.append(Goblin())
		self.monsters.append(Goblin())

	def gameOver(self) -> None:
		self.gameResult.on_next(False)
		self.gameResult.on_completed()

	def win(self) -> None:
		self.gameResult.on_next(True)
		self.gameResult.on_completed()

	# def getNextMonster(self) -> None:
	# 	if len(self.monsters) == 0:
	# 		self.win()
	# 	else:
	# 		nextMonster = self.monsters.pop()
