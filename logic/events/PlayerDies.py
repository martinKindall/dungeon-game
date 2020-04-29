from logic.events.Event import Event


class PlayerDies(Event):

	def visitGame(self, game: 'Game'):
		game.gameOver()
