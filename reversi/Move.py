from copy import copy

from Space import Space

class Move(Space):

	def __init__(self, shape, x, y, board):
		super(Move, self).__init__(x, y)
		#define shape
		self.shape = shape
		#define board
		self.board = board

	def isMoveValid(self):
		#check if the move is on the board
		if not self.board.isSpaceOnBoard(self):
			return False
		#check if the move is on an unoccupied space
		elif self.board.isSpaceOccupied(self):
			return False
		#check if the move flips at least 1 tile
		elif not self.tilesToFlip():
			return False
		else:
			return True

	def tilesToFlip(self):
		#define opposite space
		oppositeShape = 'X' if self.shape == 'O' else 'O'
		#in each direction, check tiles to flip
		directions = [
		{"x": 0, "y": 1},
		{"x": 1, "y": 0},
		{"x": 1, "y": 1},
		{"x": 1,"y": -1},
		{"x": 0, "y": -1},
		{"x": -1, "y": -1},
		{"x": -1,"y": 0},
		{"x": -1,"y": 1}
		]
		tilesToFlipList = []
		for direction in directions:
			#define the starting space, then go 1 in the direction
			currentSpace = Space(self.x, self.y)
			currentSpace.x += direction["x"]
			currentSpace.y += direction["y"]
			pendingTiles = []
			#check whether to keep adding spaces to flip or to stop
			while self.board.isSpaceOnBoard(currentSpace) and self.board.spaces[currentSpace.y][currentSpace.x] != " ":
				if self.board.spaces[currentSpace.y][currentSpace.x] == oppositeShape:
					pendingTiles.append(copy(currentSpace))
					currentSpace.x += direction["x"]
					currentSpace.y += direction["y"]
				elif self.board.spaces[currentSpace.y][currentSpace.x] == self.shape:
					tilesToFlipList += pendingTiles
					break

		return tilesToFlipList
