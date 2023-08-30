from __future__ import annotations
from basic_ai import BasicAIPlayer
from cards import Card, Rank, Suit
from player import Player
import time


class Round:
	"""A class to represent the a round of Heart.

	Methods
	-------
	check_first_player_idx(self,players) -> int
		Checks for the vary first leading player of the round
	highest_player(self, players: list[Player], trick: list[Card]) -> Player
		Check for the player that played the highest card with the leading suit

	update_score(self, player: Player, trick: list[Card]) -> int:
		Updates the round score for the player
	
	check_shooting_the_moon(self, players) -> None
		Checks if any player shoots the moon

	check_break_heart(self, card) -> None:
		Checks if hearts has been broken


	execute_turns(self, players: list, broken_hearts: bool) -> None:
		executes a turn
	
	execute_round(self, players: list) -> None:
		executes a round
	
	Methods defined here:
	__init__(self, name: str) -> None
		Constructs the necessary attributes of a round.
	"""
	def __init__(self, players: list[Player]) -> None:
		"""Constructs all the necessary attributes for a Round and executes a Hearts round.
		
		Parameters
		----------
		Players: list[Player]
			the  list of all the players
		
		Return
		------
		None
		"""
		self.players = players
		self.trick = []
		self.broken_hearts = False
		self.starting_player_idx = self.check_first_player_idx(self.players)
		# start execution
		self.execute_round(players)
		
		
	def check_first_player_idx(self,players: list[Player]) -> int:
		"""Checks for the leading player for the first turn of the round

		Parameters
		----------
		players: list[player]
			list of players

		Return
		------
		int: the index of the first leading player
		"""
		for player in players:
			if Card(Rank.Two, Suit.Clubs) in player.hand:
				return players.index(player)
		
		
	def highest_player(self, players: list[Player], trick: list[Card]) -> Player: 
		"""Check for the player that played the highest card with the leading suit

		Parameters
		----------
		players: list[player]
			list of players
		trick: list[Card]
			list of Cards in played order from trick

		Return
		------
		Player: player that will be recieving the trick and leading the next round
		"""
		lead_suit = trick[0].suit
		highest_card = trick[0]
		highest_player_idx = self.starting_player_idx
		
		for trick_idx in range(0,len(trick)):
			curr_player_idx = (self.starting_player_idx + trick_idx) % len(players)
			curr_card = trick[trick_idx]
			
			if(curr_card.suit is lead_suit) and (curr_card > highest_card):
				highest_card = curr_card
				highest_player_idx = curr_player_idx
		self.starting_player_idx = highest_player_idx
		return players[highest_player_idx]
	
	
	def update_score(self, player: Player, trick: list[Card]) -> int:
		"""Updates the round score for the player 

		Parameters
		----------
		player: Player
			player to be updated
		trick: list[Card]
			list of Cards in played order from trick

		Return
		------
		int: penalty sum of the round
		"""
		penalty_sum = 0
		for card in trick:
			if card.suit is Suit.Hearts:
				penalty_sum += 1
			elif card == Card(Rank.Queen, Suit.Spades):
				penalty_sum += 13
		player.round_score += penalty_sum	
		return penalty_sum
	
	
	def check_shooting_the_moon(self, players) -> None:
		"""Check if any player has 'shot the moon', if yes updates the score for all players

		Parameters
		----------
		players: list[player]
			list of players

		Return
		------
		None
		"""
		for player in players:
			if player.round_score == 26:
				time.sleep(0.5)
				print(f"{player} has shot the moon! Everyone else receives 26 points")
				for each_player in players:
					if each_player == player:
						player.round_score = 0
					else:
						each_player.round_score = 26
				break
						
	
	def check_break_heart(self, card) -> None:
		"""Check if hearts has been broken, if True then updates broken_hearts

		Parameters
		----------
		card: Card

		Return
		------
		None
		"""
		if (self.broken_hearts==False) and (card.suit is Suit.Hearts):
			self.broken_hearts = True
			time.sleep(0.25)
			print("Hearts have been broken!") 	
			
			
	def execute_turns(self, players: list, broken_hearts: bool) -> None:
		"""Initiates the turn execution

		Parameters
		----------
		players: list[player]
			list of players
		broken_hearts: bool
			True if hearts have been broken

		Return
		------
		None
		"""
		trick = []
		
		for i in range(len(players)):
			curr_player_idx = (self.starting_player_idx + i) % len(players)
			curr_player = players[curr_player_idx]
			
			card_played = curr_player.play_card(trick, broken_hearts)
			if i ==0:
				print(f"{curr_player} leads with \n{card_played}")
			else:
				print(f"{curr_player} plays \n{card_played}")
			trick.append(card_played)
			
			self.check_break_heart(card_played)			
		highest_player = self.highest_player(players, trick)
		
		penalty_sum = self.update_score(highest_player, trick)
		time.sleep(0.25)
		print(f"{highest_player} takes the trick. Points received: {penalty_sum}")

		
	def execute_round(self, players: list) -> None:
		"""Simulates 1 round

		Parameters
		----------
		players: list[player]
			list of players

		Return
		------
		None
		"""
		i = 0
		while len(players[0].hand) > 0:
			self.execute_turns(players, self.broken_hearts)
			i += 1
			
		self.check_shooting_the_moon(players)
		for player in players:
			player.total_score += player.round_score
			player.round_score = 0

			
			
if __name__ == "__main__":
#	players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4")]
#	players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
#	players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
#	players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
#	players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]
#	
#	Round(players)

	
#	print(players[0].hand)

#	for player in players:
#		print(f"{player}'s score: {player.round_score}")
#	for player in players:
#		print(f"{player}'s total score: {player.total_score}")
	
	pass
	
	
		
		
		