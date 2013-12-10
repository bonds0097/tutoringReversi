from termcolor import cprint

from Move import Move
from Space import Space
from Player import Player

class Board:
    def __init__(self):
        # Make empty list
        self.spaces = []
        # Append 8 lists to the empty list
        for x in range(1,9):
            self.spaces.append([])
        # For each list, append 8 empty spaces
        for list in self.spaces:
            for x in range(1,9):
                list.append(' ')
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
        #get player 1 data
        self.player1 = self.getPlayerData(1)
        #Ask for Player 2 Name & Shape.(getPlayerData)
        self.player2 = self.getPlayerData(2)
        self.setPlayer2Shape(self.player1, self.player2)

    def resetBoard(self):
        # Sets all spaces to blank
        for row in self.spaces:
            for space in row:
                space = " "
        # Sets starting positions
        self.setSpace(Space(3, 3), "O")
        self.setSpace(Space(3, 4), "X")
        self.setSpace(Space(4, 3), "X")
        self.setSpace(Space(4, 4), "O")


    def drawBoard(self, currentPlayer):
        # Set Hint Spaces
        validMoves = None
        if currentPlayer.hints:
            #Get list of Valid spaces
            validMoves = self.getValidMoves(currentPlayer)
            #Draw an asterisk(*) at each valid space
            for space in validMoves:
                self.setSpace(space, "*")
        # Calculate score
        self.calculateScore()
        # Draw score
        print("{0:8}: {1:02} | {2:8}: {3:02}".format(self.player1.name, self.player1.score, self.player2.name, self.player2.score))
        # Draw top row numbers
        print("   1  2  3  4  5  6  7  8")
        # for each row,draw row number
        for rowNumber in range(8):
            print(rowNumber + 1, end=' ')
            for space in self.spaces[rowNumber]:
                print("[" + space + "]", end='')
            print()
        # Revert Hint Spaces if needed.
        if validMoves:
            for space in validMoves:
                    self.setSpace(space, " ")



    def getPlayerData(self, playerNumber):
        playerName = input("Player {0}, What is your name?\n".format(playerNumber))
        playerShape = None
        if input("Do you want hints? (Y/N)\n").upper() == "Y":
            hints = True
        else:
            hints = False
        if playerNumber == 1:
            while not (playerShape in ["X", "O"]):
                playerShape = input("X or O? Which will it be? (X/O)\n").upper()
        playerColor = input("What color text do you want? {0}\n".format(self.colors))
        return Player(playerShape, playerName, hints, playerColor)

    def setPlayer2Shape(self, player1, player2):
        if player1.shape == "X":
            player2.shape = "O"
        else:
            player2.shape = "X"

    def isSpaceOnBoard(self, space):
        if space.x >= 0 and space.x <= 7 and space.y >= 0 and space.y <=  7:
            return True
        else:
            return False

    def isSpaceOccupied(self, space):
        if self.getSpace(space) == " ":
            return False
        else:
            return True

    def getValidMoves(self, player):
        validMoves = []
        for rowNumber in range(8):
                for columnNumber in range(8):
                    move = Move(player.shape, rowNumber, columnNumber, self)
                    if move.isMoveValid():
                        validMoves.append(move)

        return validMoves


    def calculateScore(self):
        self.player1.score = 0
        self.player2.score = 0
        for player in (self.player1, self.player2):
            for row in self.spaces:
                for space in row:
                    if space == player.shape:
                        player.score += 1


    def flipTiles(self, tilesToFlip):
        for space in tilesToFlip:
            if self.getSpace(space) == "X":
                self.setSpace(space, "O")
            else:
                self.setSpace(space, "X")

    def doMove(self, move):
        # Change the move position to right shape.
        self.setSpace(move, move.shape)
        # Flips all correct tiles.
        self.flipTiles(move.tilesToFlip())

    def getSpace(self, space):
        return self.spaces[space.y][space.x]

    def setSpace(self, space, shape):
        self.spaces[space.y][space.x] = shape
