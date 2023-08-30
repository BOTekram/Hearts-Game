from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
from copy import copy


class BetterAIPlayer(Player):
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
		if len(self.hand)!=0:
			valid_cards = []
			
			if self.check_all_hearts(self.hand) and broken_hearts==False:
				valid_cards = copy(self.hand)
			else:
				for elem in self.hand:
					if self.check_valid_play(elem, trick,broken_hearts)[0]:
						valid_cards.append(elem)
						
			if len(trick)==0:
				final = min(valid_cards)
			else:
				final = self.check_best_card(trick, valid_cards)
			self.hand.remove(final)
			return final
		else:
			raise NotImplementedError
			
			
	def pass_cards(self) -> list[Card]:
		pass_list = []
		
		for _ in range(3):
			pass_list.append(max(self.hand))
			self.hand.remove(max(self.hand))
		return pass_list
	
	
	def check_best_card(self, trick: list[Card], valid_cards: list[Card]) -> Card:
		out = max(valid_cards)
		max_in_trick = self.highest_trick_card(trick)
		leading_suit = trick[0].suit
		
		if valid_cards[0].suit is leading_suit:
			while out>max_in_trick and len(valid_cards)>1:
				valid_cards.remove(out)
				out = max(valid_cards)
		else:
			if Card(Rank.Queen, Suit.Spades) in valid_cards:
				out = Card(Rank.Queen, Suit.Spades)
		return out

			
	
		
if __name__ == "__main__":
	player = BetterAIPlayer("Test Player 1")
	player.hand = [Card(Rank.Four, Suit.Clubs), Card(Rank.Ace, Suit.Hearts), Card(Rank.King, Suit.Spades), Card(Rank.Ten, Suit.Spades)]
	
	trick, broken_hearts = [Card(Rank.Seven, Suit.Spades), Card(Rank.Eight, Suit.Spades)], False
	print(player.check_valid_play(player.hand[0], trick, broken_hearts))
	
	
	player = BetterAIPlayer("Test Player 1")
	player.hand.append(Card(Rank.Four, Suit.Clubs))
	player.hand.append(Card(Rank.Ace, Suit.Hearts))
	player.hand.append(Card(Rank.King, Suit.Spades))
	player.hand.append(Card(Rank.Ten, Suit.Spades))
	
	print(player.play_card(trick=[Card(Rank.Seven, Suit.Spades)], broken_hearts=False))
	pass