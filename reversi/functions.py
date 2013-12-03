#Name: Reversi Functions
#Author: Andrew Mickle, Lachlan Sneff

from Move import Move
from Player import Player
def getPlayerData(playerNumber):
	playerName = input("Player {0}, What is your name?\n".format(playerNumber))
	playerShape = None
	if input("Do you want hints? (Y/N)\n") == "Y":
		hints = True
	else:
		hints = False
	if playerNumber == 1:
		while not (playerShape in ["X", "O"]):
			playerShape = input("X or O? Which will it be? (X/O)\n").upper()
	return Player(playerShape, playerName, hints)

def setPlayer2Shape(player1, player2):
	if player1.shape == "X":
		player2.shape = "O"
	else:
		player2.shape = "X"

def getMove(currentPlayer, board):
	while True:
		try:
			(x, y) = input("{0}, please input the x and y coordinates for your move.\n".format(currentPlayer.name)).split()
			(x, y) = (int(x), int(y))
			break
		except ValueError:
			print("Your input was invalid. Please try again.")
	return Move(currentPlayer.shape, x-1, y-1,board)
