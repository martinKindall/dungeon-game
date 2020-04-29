from controller.Game import Game
from view import PlayerFactory
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
			lambda monster: CombatView(self.player, monster).fight()
		)

	def initWinOrLoseView(self):
		self.game.gameResult.subscribe(
			lambda result: print("You win!") if result else print("You lose!")
		)

if __name__ == '__main__':
	print("Welcome to Dungeon game!\n\n")
	Main().start()
