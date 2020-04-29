from __future__ import annotations
import abc


class Event(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def visitGame(self, game: 'Game'):
		pass
