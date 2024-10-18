from math import fabs as abs

import dice

class Card:
	def __init__(self, cost: int, sigils: list, name = None):
		self.cost = cost
		self.sigils = sigils
		self.name = name
	
	def __repr__(self):
		return f'({self.cost} {self.name}: {', '.join(self.sigils)})'

	def __str__(self):
		return __repr__(self)


def deck(deck_name = 'test'):
	decks = {
		'test': [
			Card(1, [], '1'),
			Card(2, [], '2'),
			Card(3, [], '3'),
			Card(4, [], '4'),
			Card(5, [], '5'),
			Card(6, [], '6'),
			Card(7, [], '7'),
			Card(8, [], '8'),
			Card(9, [], '9'),
		]
	}
