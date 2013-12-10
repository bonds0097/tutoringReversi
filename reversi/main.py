#Name: Reversi
#Author: Andrew Mickle, Lachlan Sneff

import random

from functions import getMove
from Board import Board
from Move import Move

#Generate Board + Middle Pieces (createBoard, resetBoard)
board = Board()
board.resetBoard()
#introduce game
print("Welcome to Reversi!")

print("Player 2, your shape is {0}".format(board.player2.shape))

#Generate random number to decide who goes first.
if random.randint(1, 2) == 1:
    currentPlayer = board.player1
else:
    currentPlayer = board.player2

print("{0} is going first!".format(currentPlayer.name))

#Start Loop
#Any Valid Moves? (getValidMoves)
while board.getValidMoves(currentPlayer):
    #Draw Board (drawBoard)
    board.drawBoard(currentPlayer)
    move = None
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
    board.doMove(move)

    # Change current player.
    if currentPlayer == board.player1:
        currentPlayer = board.player2
    else:
        currentPlayer = board.player1
#end loop
#Calculate Score & Declare Winner (calculateScore, declareWinner)
board.drawBoard(None)
score = board.calculateScore()
if score["X"] > score["O"]:
    print("X Wins!")
elif score["X"] < score["O"]:
    print("O Wins!")
else:
    print("Tie!")
