from logic.fighter.Player import Player


def createPlayer() -> 'Player':

	name = input('What is your name?: ')
	return Player(name)
