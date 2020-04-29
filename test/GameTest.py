import typing

from controller.Game import Game
from logic.fighter.Player import Player

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter

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

def gameWin() -> None:
	player = Player()
	game = Game(player)

	game.gameResult.subscribe(
		lambda result: myAssert(result)
	)

	game.nextMonsterSubject.subscribe(
		lambda monster: finishMonster(player, monster)
	)

	game.start()


def finishMonster(player: 'Fighter', monster: 'Fighter') -> None:
	while monster.hitpoints > 0:
		player.attack(monster)

def tests() -> None:
	gameOver()
	gameWin()
