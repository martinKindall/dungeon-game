import abc


class Event(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def visitGame(self, game):
		pass
