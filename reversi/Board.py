from Move import Move
from Space import Space

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

    def drawBoard(self):
        # Draw top row numbers
        print("   1  2  3  4  5  6  7  8")
        # for each row,draw row number
        for rowNumber in range(8):
            print(rowNumber + 1, end=' ')
            for space in self.spaces[rowNumber]:
                print("[" + space + "]", end='')
            print()




    def isSpaceOnBoard(self, space):
        if space.x >= 0 and space.x <= 7 and space.y >= 0 and space.y <=  7:
            return True
        else:
            return False

    def isSpaceOccupied(self, space):
        if self.setSpace(Space(y, x), " "):
            return False
        else:
            return True

    def getValidMoves(self, player):
        validMoves = []
        for rowNumber in range(8):
                for columnNumber in range(8):
                    move = Move(player["shape"], rowNumber, columnNumber, self)
                    if move.isMoveValid():
                        validMoves.append(move)

        return validMoves


    def calculateScore(self):
        scoreO = 0
        scoreX = 0
        for row in self.spaces:
            for space in row:
                if space == "O":
                    scoreO += 1
                elif space == "X":
                    scoreX += 1
        return {"X": scoreX, "O": scoreO}


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