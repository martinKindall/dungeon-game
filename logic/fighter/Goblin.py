from logic.fighter.Fighter import Fighter
from logic.weapon.Club import Club


class Goblin(Fighter):

	def __init__(self):
		super().__init__("Goblin", 5, Club(), exp=3, dodgePoints=2)
