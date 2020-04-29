import typing

from enums.Action import Action
from view import Utils

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter
	from logic.fighter.Player import Player


class CombatView:

	def __init__(self, player: 'Player', monster: 'Fighter'):
		self.player = player
		self.monster = monster

	def fight(self) -> None:
		print(self.monster, " has appeared!\n")

		while not self.monster.isDead() and not self.player.isDead():
			self.fightInteraction(self.monster, self.player)
			input("Press any key to continue...")
			Utils.clear()
			self.playerTurn()
			input("Press any key to continue...")
			Utils.clear()

	def fightInteraction(self, attacker: 'Fighter', receiver: 'Fighter') -> None:
		print(attacker, "is attacking!")
		attacker.attack(receiver)
		if receiver.dodgeState:
			print(receiver, "dodged the attack!")
		else:
			print(receiver, "received damage.")

	def playerTurn(self) -> None:
		print(self.player)
		self.displayMenu()

	def displayMenu(self) -> None:
		action = self.enterValidAction()
		print('\n')

		if action == Action.ATTACK:
			self.fightInteraction(self.player, self.monster)
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
