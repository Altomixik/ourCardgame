from player import Player
import dice
import cards

# constants
MIN_CARDS = 3


#setup
players = []
playerCount = int(input('players: '))


for i in range(playerCount):
	players.append(Player(cards.deck(), str(input('name: '))))
	

	players[-1].shuffle()
	players[-1].draw(2)

#* print(players)

# game loop
