from __future__ import annotations
import random
from copy import copy
from cards import Card, Rank, Suit
from basic_ai import BasicAIPlayer
from round import Round


class Hearts:
	def __init__(self) -> None:
		self.target_score = self.input_target_score()
		self.num_of_player = self.input_num_of_player()
		self.players = []
		
		self.execute_hearts()
		
		
	def generate_deck(self, num_of_player) -> list:
		new_deck = []
		
		for rank_val in range(2,15):
			for suit_val in range(1,5):
				new_deck.append(Card( Rank(rank_val), Suit(suit_val) ))
				
		if num_of_player == 3 or num_of_player == 5:
			new_deck.remove(Card(Rank.Two, Suit.Diamonds))
		if num_of_player == 5:
			new_deck.remove(Card(Rank.Two, Suit.Spades))
		return new_deck[:]
	
	
	def deal_card(self, players, deck_list):
		new_deck = copy(deck_list)
		random.shuffle(new_deck)
		cards_per_player = len(new_deck)//len(players)
		
		counter = 0
		while len(new_deck) > 0:
			card = random.choice(new_deck)
			curr_player = players[counter%len(players)]
			
			new_deck.remove(card)
			curr_player.hand.append(card)
			counter += 1
			
			
	def check_deal_valid(self,players) -> bool:
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
	
	
	def pass_cards(self, players, round_num):
		passing_idx_list = [None]*len(players)
		passed_cards_list = [None]*len(players)
		
		for idx in range(len(players)):
			passing_idx = (idx+round_num) % len(players)
			curr_player = players[idx]
			passed_cards = curr_player.pass_cards()
			
			passing_idx_list[idx] = passing_idx
			passed_cards_list[passing_idx] = passed_cards
			# final sub not required
			print(f"{players[idx]} passed {passed_cards} to {players[passing_idx]}")
			
		for idx in range(len(players)):
			players[idx].hand.extend(passed_cards_list[idx])
			
			
	def generate_ai_players(self, num_of_ai):
		for num in range(1, num_of_ai+1):
			self.players.append(BasicAIPlayer(f"Player {num}"))
			
			
	def game_end(self, players):
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
				return False
		else:
			return False
		
		
	def execute_hearts(self):
		round_count = 1
		game_end = False
		self.generate_ai_players(self.num_of_player)
		
		while not game_end:
			print(f"========= Starting round {round_count} =========")
			deck_list = self.generate_deck(self.num_of_player)
			
			while True:
				self.deal_card(self.players, deck_list)
				if self.check_deal_valid(self.players)==True:
					break
			for player in self.players:
				print(f"{player} was dealt {player.hand}")
			self.pass_cards(self.players, round_count)
			
			Round(self.players)
			print(f"========= End of round {round_count} =========")
			for player in self.players:
				print(f"{player}'s total score: {player.total_score}")
				
			if self.game_end(self.players):
				game_end = True
				winner_idx = self.game_end(self.players)[1]
				print(f"{self.players[winner_idx]} is the winner!")
			else:
				round_count += 1
				
				
	def input_num_of_player(self):
		input_invalid = True
		while input_invalid:
			num_of_player = int(input("Please enter the number of players (3-5):"))
			
			if num_of_player>=3 and num_of_player<=5:
				input_invalid = False
				return num_of_player
			
			
	def input_target_score(self):
		input_invalid = True
		while input_invalid:
			target_score = int(input("Please enter a target score to end the game:"))
			
			if target_score>0:
				input_invalid = False
				return target_score
			
			
if __name__ == "__main__":
	Hearts()
	

	