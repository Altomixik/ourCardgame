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
	
	def draw(self, times = 0):
		for i in times:
			self.hand.append(self.deck.pop())


	def draw_until(self, until):
		while len(self.hand) < until:
			self.hand.append(self.deck.pop())

	def place(self, card_id):
		# not in testing
		# if dice.roll() >= self.hand[card_id].cost:
		self.placements.append(self.hand.pop(card_id))

	def is_starved(self) -> bool:
		return not bool(self.placements + self.hand + self.deck)

	def attack(self, target, card_id, target_id):
		return True # dice.roll() - dice.roll() >= self.placements[card_id].cost - target.placements[target_id].cost
		