#!/usr/bin/env python3

from __future__ import annotations # for type hints of a class in itself
from enum import Enum


class Rank(Enum):
	"""A class to represent the rank of a Card.

	Methods
	-------
	Methods defined here:

	__lt__(self, other: Rank) -> bool:
		Checks if the value of the Rank object is lower than another Rank object.
	"""
	Two = 2
	Three = 3
	Four = 4
	Five = 5
	Six = 6
	Seven = 7
	Eight = 8
	Nine = 9
	Ten = 10
	Jack = 11
	Queen = 12
	King = 13
	Ace = 14
	
	
	def __lt__(self, other: Rank) -> bool:
		"""Checks if the Rank object is lower than another Rank object in terms of value.
		
		Parameters 
		----------
		other: Rank
			Rank object to compare with

		Return
		------
		True:
			if the Rank is lower than the other
		False
			if it is not lower
		"""
		if self.__class__ is other.__class__:
			return (self.value < other.value)
		else:
			raise NotImplementedError
			
			
			
class Suit(Enum):
	"""A class to represent the suit of a Card.

	Methods
	-------
	Methods defined here:

	__lt__(self, other: Suit) -> bool:
		Checks if the Suit object is lower than another Suit object in terms of value.
	"""
	triangle = 0
	Clubs = 1
	Diamonds = 2
	Spades = 3
	Hearts = 4
	
	
	def __lt__(self, other: Suit) -> bool:
		"""Compares and checks if the value of the Suit object is lower than the other Suit object.
		
		Parameters
		----------
		other: Suit
			another Suit object to compare with

		Return
		------
		True:
			if the Suit is lower than the other
		False:
			if it is not lower
		"""
		if self.__class__ is other.__class__:
			return (self.value < other.value)
		else:
			raise NotImplemented
			
			
			
class Card:
	"""A class to represent a card.
	
	Attributes
	----------
	rank : Rank
		the rank of the card
	suit : Suit
		the suit of the card

	Methods
	-------
	get_card_art(self) -> tuple[list,str]
		a tuple of the list that makes up the card art and the complete string card art

	Methods defined here:
	__init__(self, rank: Rank, suit: Suit) -> None
		Constructs the rank and suit attribute of an Card object.

	__repr__(self) -> str
		Return a string representation of the Card object.

	__str__(self) -> str:
		Return the art for the Card object.

	__eq__(self, other: Card) -> bool:
		Return True if the card is equal to another

	__lt__(self, other: Card) -> bool:
		Checks if the Card object is lower than another Card object by comparing its suit and rank.
	"""
	def __init__(self, rank: Rank, suit: Suit) -> None:
		"""Constructs all the necessary attributes for the Card object.
		
		Parameters
		----------
		rank : Rank
			rank of card
		suit : Suit
			suit of card
		
		Return
		------
		None
		"""
		self.rank = rank
		self.suit = suit
		
		
	def __repr__(self) -> str:
		"""Return a string representation of the Card object."""
		return f"{self.rank.name} of {self.suit.name}"
	
	
	def __str__(self) -> str:
		"""Returns the card art string"""
		return self.get_card_art()[1]
	
	
	def __eq__(self, other: Card) -> bool:
		"""Return True if the card are equal"""
		if (self.suit is other.suit) and (self.rank is other.rank) :
			return True
		else:
			return False
		
		
	def __lt__(self, other: Card) -> bool:
		"""Compares and checks if the the Card object is lower than the other Card object.
		Note: Prioritize suit first then rank to determine if a card is less than the other.

		Parameters
		----------
		other: Card
			Card object to compare with

		Return
		------
		True:
			if the card is lower than the other
		False:
			if it is not lower
		"""
		if self.__class__ is other.__class__:
			if self.suit < other.suit:
				return True
			elif self.suit is other.suit:
				return self.rank < other.rank
			else:
				return False
		else:
			raise NotImplementedError
			
	def get_card_art(self) -> tuple[list,str]:
		"""Constructs the card art for any card given

		Parameters
		----------
		None

		Return
		------
		returns a tuple with the following:
			list: a list of the string for card art
			str: a complete string representation of the card
		"""
		suit_art = ["♣","♦","♠","♥"]
		rank_art = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
		
		rank_art_idx = self.rank.value - 2
		suit_art_idx = self.suit.value - 1
		
		if self.rank.value == 10:
			art_list = ["┌─────┐", f"│{rank_art[rank_art_idx]}   │",f"│  {suit_art[suit_art_idx]}  │",f"│   {rank_art[rank_art_idx]}│", "└─────┘"]
		else:
			art_list = ["┌─────┐", f"│{rank_art[rank_art_idx]}    │",f"│  {suit_art[suit_art_idx]}  │",f"│    {rank_art[rank_art_idx]}│", "└─────┘"]
						
		art_str = ""
		for elem in art_list:
			art_str += (elem + "\n") 
		return (art_list,art_str)
	
	
	
	
if __name__ == "__main__":
#	print(Card(Rank.Ace,Suit.Clubs))
#	a = [Card(Rank.Ace,Suit.Clubs),Card(Rank.Eight, Suit.Diamonds)]
#	print(a)
	pass
	
	

	