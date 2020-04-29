from controller.Game import Game
from logic.fighter.Player import Player

def myAssert(boolean: bool) -> None:
	assert boolean

def gameOver() -> None:
	player = Player()
	game = Game(player)

	game.gameResult.subscribe(
		lambda result: myAssert(not result)
	)

	while player.hitpoints > 0:
		game.currentMonster.attack(player)

def tests() -> None:
	gameOver()
