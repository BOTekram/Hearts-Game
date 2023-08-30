from __future__ import annotations
from cards import Card, Rank, Suit
import time


class Player:
	"""A class to represent the all players.

	Methods
	-------
	check_suit_in_hand(self, trick: list[Card]) -> bool
		Check for any cards with the same suit as the lead card in the hand
	
	check_all_hearts(self, hand_list) -> bool
		Checks if all cards in hand are Hearts
	
	check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple[bool, str]
		Validates a chosen card for play and returns the result and an string error message

	highest_trick_card(self, trick: list[Card]) -> Card
		returns the highest card in the trick with the same suit as the lead
	
	Methods defined here:
	__init__(self, name: str) -> None
		Constructs the necessary attribute of a Player object.
	
	__repr__(self) -> str
		Return the name of the Player object.
	
	__str__(self) -> str:
		Return the name of the Player object.
	"""
	def __init__(self, name: str): 
		"""Constructs all the necessary attributes for any player object.
		
		Parameters
		----------
		name: str
			name of player
		hand: list[Card]
			the current list of cards in hand
		
		Return
		------
		None
		"""
		self.name = name
		self.hand = []
		self.round_score = 0
		self.total_score = 0
		
		
	def __repr__(self):
		return self.__str__()


	def __str__(self):
		"""Returns the name of the player"""
		return self.name


	def check_suit_in_hand(self, trick: list[Card]) -> bool:
		"""Checks if there exists a card in hand with the same suit as the lead card

		Parameters
		----------
		trick: list[Card]
			list of Cards in played order from trick

		Return
		------
		True:
			if there is a card with same suit
		False:
			if there is not
		"""
		leading_suit = trick[0].suit
		for card in self.hand:
			if card.suit is leading_suit:
				return True
		return False
	
	
	def check_all_hearts(self, hand_list) -> bool:
		"""Checks if all of the cards in hand are of suit Hearts

		Parameters
		----------
		han_list: list[Card]
			the cards in the player's hand

		Return
		------
		True:
			if all of the cards are suit Heart
		False:
			if there are none or at least 1 that is not
		"""
		is_all_hearts = True
		
		for card in hand_list:
			if card.suit is not Suit.Hearts:
				is_all_hearts = False
		return is_all_hearts
	
	
	def check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple[bool, str]:
		"""Checks if the chosen card is allowed to play

		Parameters
		----------
		card: Card
			card to validate
		trick: list[Card]
			list of Cards in played order from trick
		broken_hearts: bool
			indicates whether Hearts have been broken before

		Return
		------
		a tuple with the following types in order:
			bool: True if the card is allowed
			str: an error message depending on the validation result
		"""
		Two_of_Clubs_in_hand = Card(Rank.Two, Suit.Clubs) in self.hand
		play_Hearts = card.suit is Suit.Hearts
		play_Queen_of_Spades = ( card == Card(Rank.Queen, Suit.Spades) )
		play_Hearts_or_Queen_of_Spades 	= play_Hearts or play_Queen_of_Spades
		
		# leading
		if len(trick) == 0:		
			play_Two_Of_Clubs = (card == Card(Rank.Two, Suit.Clubs))
		
			invalid_play_1 = (Two_of_Clubs_in_hand, not play_Two_Of_Clubs)
			invalid_play_2 = (not Two_of_Clubs_in_hand, not broken_hearts, play_Hearts) 
		
			if all(invalid_play_1):
				time.sleep(0.25)
				return (False, "Player MUST lead with the two of Clubs in the first hand, You can't use other cards.")
			elif all(invalid_play_2):
				time.sleep(0.25)
				return (False, "Player cannot lead with a heart until hearts have been broken")
			
		# not leading
		else:
			is_first_round = Card(Rank.Two, Suit.Clubs) in trick
			play_follow_suit = card.suit is trick[0].suit
			suit_in_hand = self.check_suit_in_hand(trick)
		
			invalid_play_1 = (suit_in_hand, not play_follow_suit)
			invalid_play_2 = (not suit_in_hand, is_first_round, play_Hearts_or_Queen_of_Spades)
		
			if all(invalid_play_1):
				time.sleep(0.25)
				return (False, "Player still has cards from the suit of the current trick.")
			elif all(invalid_play_2):
				time.sleep(0.25)
				return (False, "Player cannot play hearts or spades on the first round.")
		time.sleep(0.25)
		return (True, "card valid")
	
	
	def highest_trick_card(self, trick: list[Card]) -> Card:
		"""This function simply checks for the leading suit of the trick and returns the highest card amongst it

		Parameters
		----------
		trick: list[Card]
			list of Cards in played order from trick

		Return
		------
		A card that is the highest while having the same suit as the lead suit
		"""
		if len(trick)>0:
			highest_card = trick[0]
			leading_suit = trick[0].suit
			
			for card in trick:
				if (card.suit is leading_suit) and (card > highest_card):
					highest_card = card
			return highest_card
		else:
			raise NotImplementedError
	
	