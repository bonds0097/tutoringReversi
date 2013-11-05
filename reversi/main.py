#Name: Reversi
#Author: Andrew Mickle, Lachlan Sneff

from functions import getPlayerData
import random
from Board import createBoard
from Board import resetBoard
from Board import drawBoard
from Move import getMove
from Move import isMoveValid
from Move import tilesToFlip
from Move import getValidMoves

print("Hello players! Welcome to Reversi!")
getPlayerData()

startingPlayer = random['1', '2']
if startingPlayer == 1:
	
createBoard()
resetBoard()
drawBoard()
getMove()
isMoveValid()
tilesToFlip()
getValidMoves()
