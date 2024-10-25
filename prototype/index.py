from player import Player
from random import shuffle
import dice
import cards
from commands import ask

# constants
MIN_CARDS = 3
PLAYER_DEFEAT_REQUIRED = 8


#setup
players = []
playerCount = int(input('players: '))


for i in range(playerCount):
	newPlayer = Player(cards.deck(), str(input('name: ')))
	shuffle(newPlayer.deck)
	newPlayer.draw_until(MIN_CARDS)
	players.append(newPlayer)

#* print(players)

# players[1].place(0)


# game loop

while playerCount > 1:
	for player in players:
		
		print(f'{player.name}\'s turn')
		print(player.placements, player.hand, sep='\n')
		action = ask('what to do?')

		if action == 'place':
			drawnIndex = ask('index?', int)
			player.place(drawnIndex)
		
		# attack
		else:
			targetName = ask('who?')
			target = list(filter(lambda p: p.name == targetName, players))[0]
			attackerId = ask('attaking card?', int)
			targetIndex = ask('target card?', int)
			
			if target.placements and player.placements:
				if player.attack(target, attackerId, targetIndex):
					print(f'{player.name}\'s {player.placements[attackerId].name} killed {target.name}\'s {target.placements[targetIndex].name}')
					target.placements.pop(targetIndex)

			elif dice.roll() >= PLAYER_DEFEAT_REQUIRED:
				players.remove(target)

		player.draw_until(MIN_CARDS)

print(players[0].name + ' won!')