import typing
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

	def monsterTurn(self) -> None:
		print(self.monster, " is attacking! You received damage.")
		self.monster.attack(self.player)

	def playerTurn(self) -> None:
		print(self.player)
		self.displayMenu()

	def displayMenu(self) -> None:
		pass
