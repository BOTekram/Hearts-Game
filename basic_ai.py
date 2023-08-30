from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
from copy import copy


class BasicAIPlayer(Player):
	"""A class to represent the basic ai players.

	Methods
	-------
	play_card(self, trick: list[Card], broken_hearts: bool) -> Card
		returns the Card that will be played for the turn 

	pass_cards(self) -> list[Card]
		returns the list of Cards that will be passed

	Methods inherited
	-----------------
	__init__(self, name: str) -> None
		Constructs the necessary attribute of a Player object.
	
	__repr__(self) -> str
		Return the name of the Player object.
	
	__str__(self) -> str:
		Return the name of the Player object.

	check_suit_in_hand(self, trick: list[Card]) -> bool
		Check for any cards with the same suit as the lead card in the hand
	
	check_all_hearts(self, hand_list) -> bool
		Checks if all cards in hand are Hearts
	
	check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple[bool, str]
		Validates a chosen card for play and returns the result and an string error message

	highest_trick_card(self, trick: list[Card]) -> Card
		returns the highest card in the trick with the same suit as the lead
	"""
	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		"""Makes the decision for the card that the ai will choose to play

		Parameters
		----------
		trick: list[Card]
			list of Cards in played order from trick
		broken_hearts: bool
			indicates whether Hearts have been broken before

		Return
		------
		A Card that will be played
		"""
		valid_cards = []
		
		if self.check_all_hearts(self.hand) and broken_hearts==False:
			valid_cards = copy(self.hand)
		else:
			for elem in self.hand:
				if self.check_valid_play(elem, trick,broken_hearts)[0]:
					valid_cards.append(elem)
		final = min(valid_cards)
		self.hand.remove(final)
		return final
	
	
	def pass_cards(self) -> list[Card]:
		"""Makes the decision for the cards that the ai will choose to pass

		Parameters
		----------
		None

		Return
		------
		A list Card that will be passed
		"""
		card_list = []
		for _ in range(3):
			card_list.append(max(self.hand))
			self.hand.remove(max(self.hand))
		return card_list
	
	
if __name__ == "__main__":
#	player = BasicAIPlayer("Test Player 1")
#	player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
#	
#	trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
#	print(player.check_valid_play(player.hand[0], trick, broken_hearts))
#
#
#	player = BasicAIPlayer("Test Player 1")
#	player.hand.append(Card(Rank.Four, Suit.Clubs))
#	player.hand.append(Card(Rank.Ace, Suit.Hearts))
#	player.hand.append(Card(Rank.King, Suit.Spades))
#	player.hand.append(Card(Rank.Ten, Suit.Spades))
#
#	print(player.play_card(trick=[Card(Rank.Seven, Suit.Spades)], broken_hearts=False))
	pass
	