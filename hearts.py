from __future__ import annotations

"""
Author:Ekramul Islam
"""

import random   
from copy import copy
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from better_ai import BetterAIPlayer
from human import Human
from round import Round
import time 


class Hearts:
	"""A class to represent the a game of Heart.

	Methods
	-------
	generate_deck(self, num_of_player) -> list:
		Generate a new deck list

	deal_card(self, players, deck_list):
		Deals the cards from the deck to each player's hand
	
	check_deal_valid(self,players) -> bool:
		Checks if the deal is valid
	
	pass_cards(self, players, round_num) -> None:
		Simulates the passing cards procedure in the round
	
	generate_players(self, num_of_players) -> None:
		Generates the player objects based on the number of players
	
	game_end(self, players) -> tuple[bool,int]:
		Checks if the round has ended
	
	execute_hearts(self):
		Executes a game of hearts
	
	input_num_of_player(self):
		prompts and gets the number of players
	
	input_target_score(self):
		Prompts and gets the target score limit
		
	Methods defined here:
	__init__(self) -> None
		Constructs the necessary attributes of a Hearts game.
	"""
	def __init__(self) -> None:
		"""Constructs all the necessary attributes for a Round and executes a Hearts round"""
		print("Welcome to ♥ HEARTS ♥")
		self.target_score = self.input_target_score()
		self.num_of_player = self.input_num_of_player()
		self.players = []
		#start the game
		self.execute_hearts()
		
	
	def generate_deck(self, num_of_player) -> list:
		"""Generate a new deck list 

		Parameters
		----------
		num_of_player: int
			number of players 

		Return
		------
		list: list of all the cards in the deck
		"""
		new_deck = []
		
		for rank_val in range(2,15):
			for suit_val in range(1,5):
				new_deck.append(Card( Rank(rank_val), Suit(suit_val) ))

		if num_of_player == 3 or num_of_player == 5:
			new_deck.remove(Card(Rank.Two, Suit.Diamonds))
		if num_of_player == 5:
			new_deck.remove(Card(Rank.Two, Suit.Spades))
		return copy(new_deck)
	
	
	def deal_card(self, players, deck_list):
		"""Deals the cards from the deck to each player's hand

		Parameters
		----------
		players: list[player]
			list of players
		deck_list: list[Card]
			list af all the cards in the deck

		Return
		------
		None
		"""
		new_deck = copy(deck_list)
		random.shuffle(new_deck)
		cards_per_player = len(new_deck)//len(players)
		counter = 0
		while len(new_deck) > 0:
			card = new_deck[-1]
			curr_player = players[counter%len(players)]
			
			new_deck.pop()
			curr_player.hand.append(card)
			counter += 1
		
		
	def check_deal_valid(self,players) -> bool:
		"""Checks if the deal is valid

		Parameters
		----------
		players: list[player]
			list of players

		Return
		------
		bool: True if the deal is valid
		"""
		for player in players:
			flag = False
			if Card(Rank.Queen, Suit.Spades) in player.hand:
				flag = True		
			else:
				for card in player.hand:
					if card.suit is Suit.Hearts:
						flag = True
			if flag == False:
				return False
		return True
	
	
	def pass_cards(self, players, round_num) -> None:
		"""Simulates the passing cards procedure in the round

		Parameters
		----------
		players: list[player]
			list of players
		round_num: int
			the current round count

		Return
		------
		None
		"""
		passing_idx_list = [None]*len(players)
		passed_cards_list = [None]*len(players)

		for idx in range(len(players)):
			passing_idx = (idx+round_num) % len(players)
			curr_player = players[idx]
			passed_cards = curr_player.pass_cards()
			
			passing_idx_list[idx] = passing_idx
			passed_cards_list[passing_idx] = passed_cards
			

		for idx in range(len(players)):
			players[idx].hand.extend(passed_cards_list[idx])
			players[idx].hand.sort()
			
	
	def generate_players(self, num_of_players) -> None:
		"""Generates the player objects based on the number of players

		Parameters
		----------
		num_of_players: int
			number of players

		Return
		------
		None
		"""
		self.players.append(Human())
		self.players.append(BasicAIPlayer("Player 2"))
		for num in range(3,int(num_of_players)+1):
			self.players.append(BetterAIPlayer(f"Player {num}"))
	
						
	def game_end(self, players) -> tuple[bool,int]:
		"""Checks if the round has ended

		Parameters
		----------
		players: list[player]
			list of players

		Return
		------
		a tuple of the following:
			bool: True if the round has ended
			int: the winner index in players
		"""
		is_game_end = False
		for player in players:
			if player.total_score >= self.target_score:
				is_game_end = True
				
		if is_game_end == True:
			winner_idx = 0
			winner_count = 1
			min_score = players[0].total_score
			
			for idx in range(1, len(players)):
				if players[idx].total_score < min_score:
					winner_idx = idx
					min_score = players[idx].total_score
					winner_count = 1
				elif  players[idx].total_score == min_score:
					winner_count += 1
			if winner_count == 1:
				return (True, winner_idx)
			else:
				return (False,None)
		else:
			return (False,None)
				
				
	def execute_hearts(self):
		"""Executes a game of hearts"""
		round_count = 1
		game_end = False
		self.generate_players(self.num_of_player)
		
		while not game_end:
			time.sleep(0.25)
			print(f"========= Starting round {round_count} =========")
			deck_list = self.generate_deck(self.num_of_player)
			
			while True:
				self.deal_card(self.players, deck_list)
				if self.check_deal_valid(self.players)==True:
					for player in self.players:
						player.hand.sort()
					break
			self.pass_cards(self.players, round_count)
			time.sleep(0.25)
			print("Cards have been passed")
			Round(self.players)
			time.sleep(0.25)
			print(f"========= End of round {round_count} =========")
			for player in self.players:
				print(f"{player}'s total score: {player.total_score}")
			
			if self.game_end(self.players)[0]:
				game_end = True
				winner_idx = self.game_end(self.players)[1]
				print(f"{self.players[winner_idx]} is the winner!")
			else:
				round_count += 1
	

	def input_num_of_player(self):
		"""prompts and gets the number of players

		Parameters
		----------
		None

		Return
		------
		int: the number of players
		"""
		input_invalid = True
		while input_invalid:
			num_of_player = input("Please enter the number of players (3-5): ")
			
			if not num_of_player.isdigit():
				continue
			elif int(num_of_player)>=3 and int(num_of_player)<=5:
				input_invalid = False
				return int(num_of_player)
			
			
	def input_target_score(self):
		"""Prompts and gets the target score limit

		Parameters
		----------
		None

		Return
		------
		int: the target score
		"""
		input_invalid = True
		while input_invalid:
			target_score = input("Please enter a target score to end the game(at least 10): ")
			
			if not target_score.isdigit():
				continue
			elif int(target_score)>=10:
				input_invalid = False
				return int(target_score)
			
			
			
if __name__ == "__main__":
	Hearts()
	pass
	
	
	

	
		

	
	
	
	