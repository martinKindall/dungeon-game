from logic.fighter.Fighter import Fighter
from logic.weapon.Sword import Sword


class Goblin(Fighter):

	def __init__(self):
		super().__init__("Goblin", 5, Sword(), 3)
