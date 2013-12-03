#Name: Reversi Functions
#Author: Andrew Mickle, Lachlan Sneff

from Move import Move
from Player import Player

def getMove(currentPlayer, board):
	while True:
		try:
			(x, y) = input("{0}, please input the x and y coordinates for your move.\n".format(currentPlayer.name)).split()
			(x, y) = (int(x), int(y))
			break
		except ValueError:
			print("Your input was invalid. Please try again.")
	return Move(currentPlayer.shape, x-1, y-1,board)
