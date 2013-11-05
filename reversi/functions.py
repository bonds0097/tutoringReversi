#Name: Reversi Functions
#Author: Andrew Mickle, Lachlan Sneff

from Move import Move

def getPlayerData(playerNumber):
	playerName = input("Player {0}, What is your name?\n", playerNumber)
	playerShape = None

	if playerNumber == 1:
		while not (playerShape in ["X", "O"]):
			playerShape = input("X or O? Which will it be? (X/O)\n").upper()

	return {"name": playerName, "shape": playerShape}


def setPlayer2Shape(player1, player2):
	if player1["shape"] == "X":
		player2["shape"] = "O"
	else:
		player2["shape"] = "X"

def getMove(currentPlayer, board):
	(x, y) = input("Please input the x and y coordinates for your move.\n")
	return Move(currentPlayer["shape"], x-1, y-1, board)