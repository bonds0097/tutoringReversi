#Name: Reversi
#Author: Andrew Mickle, Lachlan Sneff

import random

from functions import getPlayerData
from functions import setPlayer2Shape
from functions import getMove
from board import Board
from Move import Move

#introduce game
print("Welcome to Reversi!")
#get player 1 data
player1 = getPlayerData(1)

#Ask for Player 2 Name & Shape.(getPlayerData)
player2 = getPlayerData(2)
setPlayer2Shape(player1, player2)
print("Player 2, your shape is {0}".format(player2["shape"]))

#Generate random number to decide who goes first.
if random.randint(1, 2) == 1:
    currentPlayer = player1
else:
    currentPlayer = player2

print("{0} is going first!".format(currentPlayer["name"]))

#Generate Board + Middle Pieces (createBoard, resetBoard)
board = Board()
board.resetBoard()
#Start Loop
#Any Valid Moves? (getValidMoves)
while board.getValidMoves():
    #Draw Board (drawBoard)
    board.drawBoard()
    #Start loop
    while True:
        #Ask for move (getMove)
        move = getMove(currentPlayer, board)
        #Check for Valid Move (isMoveValid)
        if move.isMoveValid():
            break
        else:
            print("Invalid Move. Try again.")
    #End Loop
    #Flip opponent pieces(tiles to flip)
    board.flipTiles(move.tilesToFlip())

    # Change current player.
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1
#end loop
#Calculate Score & Declare Winner (calculateScore, declareWinner)
score = board.calculateScore()
if score["X"] > score["O"]:
    print("X Wins!")
elif score["X"] < score["O"]:
    print("O Wins!")
else:
    print("Tie!")
