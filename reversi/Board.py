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
        self.spaces[3][3] = "O"
        self.spaces[3][4] = "X"
        self.spaces[4][3] = "X"
        self.spaces[4][4] = "O"

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
        if x >= 0 <= 7 and y >= 0 <=  7:
            return true
        else:
            return false

    # def isSpaceOccupied():

    # def getValidMoves(self):

    # def calculateScore(self):

    # def flipTiles(tilesToFlip):
