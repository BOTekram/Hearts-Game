
from __future__ import annotations
from basic_ai import*
from cards import Card, Rank, Suit


class Round:
	
	
	def __init__(self, players: list[Player]) -> None:
		self.players = players
		self.trick = []
		self.broken_hearts = False
		self.starting_player_idx = self.check_first_player(self.players)
		
		# start execution
		self.execute_round(players)
		
		
	# empty trick
	def check_first_player(self,players) -> int:
		for player in players:
			if Card(Rank.Two, Suit.Clubs) in player.hand:
				return players.index(player)
		raise NotImplementedError
		
	def highest_player(self, players: list, trick) -> Player: 
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
	
	
	def update_score(self, player, trick) -> int:
		penalty_sum = 0
		for card in trick:
			if card.suit is Suit.Hearts:
				penalty_sum += 1
			elif card == Card(Rank.Queen, Suit.Spades):
				penalty_sum += 13
		player.round_score += penalty_sum	
		return penalty_sum
	
	
	def check_shooting_the_moon(self, players):
		for player in players:
			if player.round_score == 26:
				print(f"{player} has shot the moon! Everyone else receives 26 points")
				for each_player in players:
					if each_player == player:
						player.round_score = 0
					else:
						each_player.round_score = 26
						
						
	def check_break_heart(self, card):
		if (self.broken_hearts==False) and (card.suit is Suit.Hearts):
			self.broken_hearts = True
			print("Hearts have been broken!") 	
			
	def execute_turns(self, players: list, broken_hearts: bool):
		
		trick = []
		
		for i in range(len(players)):
			curr_player_idx = (self.starting_player_idx + i) % len(players)
			curr_player = players[curr_player_idx]
			
			card_played = curr_player.play_card(trick, broken_hearts)
			print(f"{curr_player} plays {card_played}")
			trick.append(card_played)
			
			self.check_break_heart(card_played)			
		highest_player = self.highest_player(players, trick)
		
		penalty_sum = self.update_score(highest_player, trick)
		print(f"{highest_player} takes the trick. Points received: {penalty_sum}")
		
		
	def execute_round(self, players: list):
		i = 0
		
		while len(players[0].hand) > 0:
			self.execute_turns(players, self.broken_hearts)
			i += 1
			
		# print end of round stats to see player objects updated
		self.check_shooting_the_moon(players)
		for player in players:
			player.total_score += player.round_score
			player.round_score = 0
			
			
			
if __name__ == "__main__":
	players = [BasicAIPlayer("Player 1"), BasicAIPlayer("Player 2"), BasicAIPlayer("Player 3"), BasicAIPlayer("Player 4")]
	players[0].hand = [Card(Rank.Four, Suit.Diamonds), Card(Rank.King, Suit.Clubs), Card(Rank.Nine, Suit.Clubs), Card(Rank.Ace, Suit.Hearts)]
	players[1].hand = [Card(Rank.Two, Suit.Clubs), Card(Rank.Four, Suit.Spades), Card(Rank.Nine, Suit.Spades), Card(Rank.Six, Suit.Diamonds)]
	players[2].hand = [Card(Rank.Seven, Suit.Diamonds), Card(Rank.Ace, Suit.Spades), Card(Rank.Jack, Suit.Diamonds), Card(Rank.Queen, Suit.Spades)]
	players[3].hand = [Card(Rank.Queen, Suit.Hearts), Card(Rank.Jack, Suit.Clubs), Card(Rank.Queen, Suit.Diamonds), Card(Rank.King, Suit.Hearts)]
	
	Round(players)
	pass
	