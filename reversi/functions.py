#Name: Reversi Functions
#Author: Andrew Mickle, Lachlan Sneff


def getPlayerData(playerNumber):
	playerName = input("What is your name?\n")
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