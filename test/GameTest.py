import typing

from controller.Game import Game
from logic.fighter.Player import Player

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter

def myAssert(boolean: bool) -> None:
	assert boolean

def gameOver() -> None:
	player = Player("", dodgePoints=0)
	game = Game(player)

	game.gameResult.subscribe(
		lambda result: myAssert(not result)
	)

	while player.hitpoints > 0:
		game.currentMonster.attack(player)

def gameWin() -> None:
	player = Player("", dodgePoints=0)
	game = Game(player)

	game.gameResult.subscribe(
		lambda result: myAssert(result)
	)

	game.nextMonsterNameSubject.subscribe(
		lambda monster: finishMonster(player, monster)
	)

	game.start()

def gameWinNotUsingModelDirectly() -> None:
	player = Player("", dodgePoints=0)
	game = Game(player)

	game.gameResult.subscribe(
		lambda result: myAssert(result)
	)

	game.nextMonsterNameSubject.subscribe(
		lambda monster: finishMonsterUsingGame(game)
	)

	game.start()

def finishMonster(player: 'Fighter', monster: 'Fighter') -> None:
	while not monster.isDead():
		player.attack(monster)

def finishMonsterUsingGame(game: Game) -> None:
	while not game.currentMonsterIsDead():
		game.playerAttackCurrentMonster()

def tests() -> None:
	gameOver()
	gameWin()
	gameWinNotUsingModelDirectly()
