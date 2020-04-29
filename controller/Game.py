from typing import List
import typing
from rx.subject import Subject

from logic.fighter.Goblin import Goblin

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter
	from logic.events.Event import Event
	from logic.fighter.Player import Player

class Game:

	def __init__(self, player: 'Player'):
		self.player = player
		self.gameResult: Subject[bool] = Subject()
		self.nextMonsterSubject: Subject['Fighter'] = Subject()

		self.currentMonster: 'Fighter' = Goblin()
		self.monsters: List['Fighter'] = list()
		self.monsters.append(Goblin())
		self.monsters.append(Goblin())

		self.playerDisposable = self.player.eventObservable.subscribe(self.accept)
		self.currentMonsterDisposable = self.currentMonster.eventObservable.subscribe(self.accept)

	def gameOver(self) -> None:
		self.release()

		self.gameResult.on_next(False)
		self.gameResult.on_completed()

	def win(self) -> None:
		self.release()

		self.gameResult.on_next(True)
		self.gameResult.on_completed()

	def accept(self, event: 'Event') -> None:
		event.visitGame(self)

	def release(self) -> None:
		self.playerDisposable.dispose()
		self.currentMonsterDisposable.dispose()

	def goNextMonster(self) -> None:
		if len(self.monsters) == 0:
			self.win()
		else:
			nextMonster = self.monsters.pop()
			self.currentMonsterDisposable.dispose()
			self.currentMonsterDisposable = nextMonster.eventObservable.subscribe(self.accept)
			self.nextMonsterSubject.on_next(nextMonster)

	def start(self) -> None:
		self.nextMonsterSubject.on_next(self.currentMonster)
