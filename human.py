from __future__ import annotations
from cards import Card, Rank, Suit
from player import Player
import time

class Human(Player):
	"""A class to represent the human players.

	Methods
	-------
	play_card(self, trick: list[Card], broken_hearts: bool) -> Card
		returns the Card that will be played for the turn 

	pass_cards(self) -> list[Card]
		returns the list of Cards that will be passed
	
	Methods defined here:
	__init__(self) -> None
		gets the player name from user and inherits the attributes of Player class
	
	
			

	Methods inherited
	-----------------
	__init__(self, name: str) -> None
		Constructs the hand list and score attributes for the object.
	
	__repr__(self) -> str
		Return the name of the object.
	
	__str__(self) -> str:
		Return the name of the object.

	check_suit_in_hand(self, trick: list[Card]) -> bool
		Check for any cards with the same suit as the lead card in the hand
	
	check_all_hearts(self, hand_list) -> bool
		Checks if all cards in hand are Hearts
	
	check_valid_play(self, card: Card, trick: list[Card], broken_hearts: bool) -> tuple[bool, str]
		Validates a chosen card for play and returns the result and an string error message

	highest_trick_card(self, trick: list[Card]) -> Card
		returns the highest card in the trick with the same suit as the lead
	"""
	
	
	def __init__(self) -> None: 
		"""Constructs all the necessary attributes for the human player object.
		
		Parameters
		----------
		None

		Attributes:
		name: str
			prompts and gets the name of player from the user
		
		Attributes inherited:
		hand: list[Card]
			the current list of cards in hand
		round_score: int
			the total score gained in this round
		total_score: int
			the total score for all rounds

		Return
		------
		None
		"""
		self.name = input("Please enter your player name: ")
		super().__init__(self.name)
		
	def play_card(self, trick: list[Card], broken_hearts: bool) -> Card:
		"""Returns the card based on the player's decision

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
		
		time.sleep(0.5)
		print("Current trick:\n" + self.get_card_list_art(trick, False))
		time.sleep(0.5)
		self.hand.sort()
		print("Current hand:\n" + self.get_card_list_art(self.hand, True))
			
		while True:
			time.sleep(0.25)
			card_idx = input('Select a card to play: ')
				
			if card_idx.isdigit():
				if int(card_idx)>=0 and int(card_idx)<len(self.hand):
					card_to_check = self.hand[int(card_idx)]
					
					if self.check_valid_play(card_to_check, trick, broken_hearts)[0]:
						self.hand.remove(card_to_check)
						return card_to_check
					else:
						time.sleep(0.25)
						print(self.check_valid_play(card_to_check, trick, broken_hearts)[1])
						continue
				else:
					continue
			else:
				time.sleep(0.25)
				print(f"You can only input one integer between 0 and {len(self.hand)-1}")
	
	def check_no_duplicate_int(self, any_list: list) -> bool:
		"""Checks if there exists a duplicate the input recieved or an unwanted input type

		Parameters
		----------
		any_trick: list
			list of Cards to check

		Return
		------
		True:
			if there is no duplicates and are all integers
		False:
			there are duplicates or exist any input that is not an int
		"""
		no_duplicate = True
		for elem in any_list:
			if elem.isdigit()==False:
				return False
			if any_list.count(elem) > 1:
				no_duplicate = False
		return no_duplicate
		
	def pass_cards(self) -> list[Card]:
		"""Gets the decision for the cards that will be passed from the player

		Parameters
		----------
		None

		Return
		------
		A list Card that will be passed
		"""
		time.sleep(0.5)
		print("Current hand:\n" + self.get_card_list_art(self.hand, True))
		
		input_valid = False
		while not input_valid:
			time.sleep(0.25)
			card_idx_input = input(f"Select three cards to pass off (e.g. '0, 4, 5') : ")
			card_idx_list = card_idx_input.replace(" ","").split(",")
			
			if len(card_idx_list)==3 and self.check_no_duplicate_int(card_idx_list):
				input_valid = True
				for idx in card_idx_list:
					if int(idx)<0 or int(idx)>=len(self.hand):
						input_valid = False
			if input_valid == False:
				time.sleep(0.25)
				print(f"You can only input three unique integers between 0 and {len(self.hand)-1}")
		out = []
		for idx in card_idx_list:
			out.append(self.hand[int(idx)])
		for card in out:
			self.hand.remove(card)
		return out
	
	def get_card_list_art(self, card_list: list[Card], add_idx: bool) -> str:
		"""Constructs the art for multiple cards that will be displayed side by side 

		Parameters
		----------
		card_list: list[Card]
			list of cards to display
		add_idx: bool
			True:
				if the index of cards is needed to be shown at the bottom of each card
			False:
				no index will be displayed
		Return
		------
		A list Card that will be passed
		"""
		if len(card_list)>0:
			temp = []
			out = ""
			
			for card in card_list:
				temp.append(card.get_card_art()[0])
				
			if add_idx == True:
				for row in range(len(temp[0])+1):
					for card_i in range(len(card_list)):
						if row == len(temp[0]):
							if card_i >= 10:
								out+= f"   {card_i}  "
							else:
								out+= f"   {card_i}   "
						else:
							out += (temp[card_i][row])
					out += "\n"
			else:
				for row in range(len(temp[0])):
					for card_i in range(len(card_list)):
						out += (temp[card_i][row])
					out += "\n"
			return out
		else:
			return "You are leading, please choose a leading card."
		
			

if __name__ == "__main__":
#	player = Human()
#	player.hand.append(Card(Rank.Four, Suit.Clubs))
#	player.hand.append(Card(Rank.Ace, Suit.Hearts))
#	player.hand.append(Card(Rank.King, Suit.Spades))
#	player.hand.append(Card(Rank.Ten, Suit.Spades))
	
#	player.play_card(trick=[Card(Rank.Seven, Suit.Spades)], broken_hearts=False)
#	print(player.pass_cards())
#	print(player.hand)
#	a = [Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts),Card(Rank.Ten, Suit.Hearts)]
#	b = player.get_card_list_art(a, True)
#	print(b)
	
#	player.hand
	pass
		
	