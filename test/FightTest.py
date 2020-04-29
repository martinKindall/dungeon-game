from logic.fighter.Fighter import Fighter
from logic.fighter.Goblin import Goblin
from logic.fighter.Player import Player


def fighterDoesDamage(fighter: Fighter):
	goblin = Goblin()

	for _ in range(3):
		fighter.attack(goblin)

	assert fighter.hitpoints > goblin.hitpoints
	assert goblin.hitpoints == 0

def playerCanHeal():
	player = Player()
	goblin = Goblin()

	goblin.attack(player)
	playerHitpoints = player.hitpoints
	player.selfHeal()
	assert player.hitpoints > playerHitpoints

if __name__ == '__main__':
	fighterDoesDamage(Goblin())
	fighterDoesDamage(Player())
	print("Tests passed")
