import typing

from enums.Action import Action
from view import Utils

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter
	from logic.fighter.Player import Player
	from controller.Game import Game


class CombatView:

	def __init__(self, game: 'Game', player: 'Player', monster: 'Fighter'):
		self.player = player
		self.monster = monster
		self.game = game

	def fight(self) -> None:
		print(self.monster, " has appeared!\n")

		while not self.game.currentMonsterIsDead():
			print('{} is attacking!'.format(self.monster))
			print(self.game.currentMonsterAttackPlayer())
			input("Press any key to continue...")
			Utils.clear()
			self.playerTurn()
			input("Press any key to continue...")
			Utils.clear()

	def playerTurn(self) -> None:
		print(self.player)
		self.displayMenu()

	def displayMenu(self) -> None:
		action = self.enterValidAction()
		print('\n')

		if action == Action.ATTACK:
			print(self.game.playerAttackCurrentMonster())
		elif action == Action.HEAL:
			print(self.player.name + ' self heals.')
			self.player.selfHeal()
		elif action == Action.QUIT:
			print(self.player.name + ' abandons game. See you soon!')
			exit()

	def enterValidAction(self) -> Action:
		while True:
			actionList: typing.List[Action] = [action for action in Action]
			for action in actionList:
				print(action, "): ", action.description())
			try:
				userAction = Action.strToAction(input(" -> Enter an action: "))
			except ValueError:
				print("Not a valid action")
			else:
				return userAction
