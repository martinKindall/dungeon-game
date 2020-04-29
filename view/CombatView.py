import typing

from enums.Action import Action

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter
	from logic.fighter.Player import Player


class CombatView:

	def __init__(self, player: 'Player', monster: 'Fighter'):
		self.player = player
		self.monster = monster

	def fight(self) -> None:
		print(self.monster, " has appeared!")

		while not self.monster.isDead() and not self.player.isDead():
			self.monsterTurn()
			input("Press any key to continue...")
			self.playerTurn()
			input("Press any key to continue...")

	def monsterTurn(self) -> None:
		print(self.monster, "is attacking! You received damage.")
		self.monster.attack(self.player)

	def playerTurn(self) -> None:
		print(self.player)
		self.displayMenu()

	def displayMenu(self) -> None:
		action = self.enterValidAction()

		if action == Action.ATTACK:
			print(self.player.name + ' attacked ' + self.monster.name)
			self.player.attack(self.monster)
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
