import random

params = {'starting_path': (1,4),
		  'war_path': (5,12),
		  'final_path': (13,14),
	      'start': 0, 'end': 15,
		  'number_of_pieces': 7,
		  'rosettas': [4,8,14]}

class Player:
	def __init__(self, number, params):
		self.number = number
		self.pieces = []
		for i in range (params['number_of_pieces']):
			self.pieces.append(params['start'])

class Board:
	def __init__(self, params):
		self.player1 = Player(1,params)
		self.player2 = Player(2,params)

	def print_board(self):
		player1_print_buffer = []
		player2_print_buffer = []
		for i in range(params['start']+1,params['end']):
			if i in params['rosettas']:
				player1_print_buffer.append('R')
				player2_print_buffer.append('R')
			else:
				player1_print_buffer.append('O')
				player2_print_buffer.append('O')

			if i > 0:
				if i in self.player1.pieces:
					if player1_print_buffer[i-1] == 'R':
						player1_print_buffer[i-1] = 'R¹'
					else:
						player1_print_buffer[i-1] = '1'
				if i in self.player2.pieces:
					if player2_print_buffer[i-1] == 'R':
						player2_print_buffer[i-1] = 'R²'
					else:
						player2_print_buffer[i-1] = '2'

		print(player1_print_buffer)
		print(player2_print_buffer)

	def roll_dice(self):
		prob = random.random()
		if prob <= 0.0625:
			return 0
		elif prob <= 0.3125:
			return 1
		elif prob <= 0.6875:
			return 2
		elif prob <= 0.9375:
			return 3
		else:
			return 4

	def move(self,player,piece,position):
		if position in player.pieces:
			print('You cant put two pieces in the same position')
			return 0
		war_path = params['war_path']
		if position in range(war_path[0],war_path[1],1):
			if player.number == 1:
				opponent = self.player2
			else:
				opponent = self.player1
			if position in opponent.pieces:
				return self.war_move(player,opponent,piece,position)
		player.pieces[piece] = position
		return 1

	def war_move(self,attacker,defender,attacker_píece,position):
		if position in params['rosettas']:
			print("You cant attack a piece in a protected position")
			return 0
		defender_piece = defender.pieces.index(position)
		defender.pieces[defender_piece] = 0
		attacker.pieces[attacker_píece] = position
		return 1

if __name__ == '__main__':
    g = Board(params)
    g.print_board()
    g.move(g.player1,1,8)
    g.print_board()
    print(g.roll_dice())