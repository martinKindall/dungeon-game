import typing
from logic.events.Event import Event

if typing.TYPE_CHECKING:
	from controller.Game import Game

class PlayerDies(Event):

	def visitGame(self, game: 'Game'):
		game.gameOver()
