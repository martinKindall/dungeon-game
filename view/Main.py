from controller.Game import Game
from view import PlayerFactory, Utils
from view.CombatView import CombatView


class Main:

	def __init__(self):
		self.player = PlayerFactory.createPlayer()
		self.game = Game(self.player)

	def start(self):
		self.initCombatView()
		self.initWinOrLoseView()
		self.game.start()

	def initCombatView(self):
		self.game.nextMonsterSubject.subscribe(
			lambda monster: self.clearScreenAndNextMonster(monster)
		)

	def initWinOrLoseView(self):
		self.game.gameResult.subscribe(
			lambda result: self.winView() if result else self.loseView()
		)

	def winView(self) -> None:
		print("You win!")
		exit()

	def loseView(self) -> None:
		print("You lose...")
		exit()

	def clearScreenAndNextMonster(self, monster) -> None:
		Utils.clear()
		CombatView(self.player, monster).fight()


if __name__ == '__main__':
	print("Welcome to Dungeon game!\n\n")
	Main().start()
