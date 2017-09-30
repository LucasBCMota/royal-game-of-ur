import random

params = {'starting_path': (1,4),
		  'war_path': (5,12),
		  'final_path': (13,14),
	      'start': 0, 'end': 15,
		  'number_of_pieces': 7,
		  'rosettas': [4,8,14]}

class Player:
	def __init__(self, params):
		self.pieces = []
		for i in range (params['number_of_pieces']):
			self.pieces.append(params['start'])

class Board:
	def __init__(self, params):
		self.player1 = Player(params)
		self.player2 = Player(params)

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
					player1_print_buffer[i] = '1'
				if i in self.player2.pieces:
					player2_print_buffer[i] = '2'

		print(player1_print_buffer)
		print(player2_print_buffer)


if __name__ == '__main__':
    g = Board(params)
    g.print_board()