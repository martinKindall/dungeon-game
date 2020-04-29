from rx.subject import Subject

from logic.fighter.Fighter import Fighter
from logic.fighter.Player import Player


class Game:

	def __init__(self, player: Player):
		self.player = player
		self.gameResult: Subject[bool] = Subject()
		self.nextFighter: Subject[Fighter] = Subject()
