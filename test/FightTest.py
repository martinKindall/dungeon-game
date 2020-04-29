from logic.fighter.Goblin import Goblin


def fighterDoesDamage():
	goblin1 = Goblin()
	goblin2 = Goblin()

	for _ in range(3):
		goblin1.attack(goblin2)

	assert goblin1.hitpoints > goblin2.hitpoints
	assert goblin2.hitpoints == 0

if __name__ == '__main__':
	fighterDoesDamage()
	print("Tests passed")
