import typing
from logic.fighter.Goblin import Goblin
from logic.fighter.Player import Player

if typing.TYPE_CHECKING:
	from logic.fighter.Fighter import Fighter

def fighterDoesDamage(fighter: 'Fighter'):
	goblin = Goblin(dodgePoints=0)

	for _ in range(3):
		fighter.attack(goblin)

	assert fighter.hitpoints > goblin.hitpoints
	assert goblin.hitpoints == 0

def playerCanHeal():
	player = Player("", dodgePoints=0)
	goblin = Goblin(dodgePoints=0)

	goblin.attack(player)
	playerHitpoints = player.hitpoints
	player.selfHeal()
	assert player.hitpoints > playerHitpoints

def tests() -> None:
	fighterDoesDamage(Goblin(dodgePoints=0))
	fighterDoesDamage(Player("", dodgePoints=0))

if __name__ == '__main__':
	tests()
	print("Tests passed")
