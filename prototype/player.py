import cards
import dice

from random import shuffle

class Player:
	def __init__(self, starting_deck, name = 'anon'):
		self.placements = []
		self.hand = []
		self.deck = starting_deck
		self.buffs = 0
		self.name = name

	def __repr__(self):
		return f'\n{self.name}:\n\tplacements: {self.placements}\n\thand: {self.hand}\n\tdeck: {self.deck}'
	
	
	def draw(self, times = 1):
		for i in range(times):
			self.hand.append(self.deck.pop())

	def place(self, card_id):
		#* not in testing
		# if dice.roll() >= self.hand[card_id].cost:
		self.placements.append(self.hand.pop(card_id))

	def is_starved(self) -> bool:
		return not bool(self.placements + self.hand + self.deck)

	def attack(self, card_id, target, target_id):
		throw_result = dice.roll() - dice.roll() >= self.placements[card_id].cost - target.placements[target_id].cost
		if throw_result:
			target.placements.pop(target_id)
			print('you killed a card')
		else:
			print('you failed an attack')
	
	def shuffle(self):
		shuffle(self.deck)