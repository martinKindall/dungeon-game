import abc
import typing

if typing.TYPE_CHECKING:
	from controller.Game import Game

class Event(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def visitGame(self, game: 'Game'):
		pass
