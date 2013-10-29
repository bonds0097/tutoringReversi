class Move:

	def __init__(self, shape, x, y, board):
		#define shape
		self.shape = "shape"
		#define x
		self.x = "x"
		#define y
		self.y = "y"
		#define board
		self.board = "board"

	def isMoveValid(self, currentPlayer):
		#check if the move is on the board
		if not self.board.isMoveOnBoard(self):
			return False
		#check if the move is on an unoccupied space
		elif self.board.isSpaceOccupied(self):
			return False
		#check if the move flips at least 1 tile
		elif self.board.tilesToFlip(self) <= 0:
			return False
		else:
			return True
		
	def tilesToFlip(self):
		#define opposite space
		oppositeSpace = 'X' if move.shape == 'O' else 'O'
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
			currentSpace = {"x": self.x, "y": self.y}
			currentSpace["x"] += direction["x"]
			currentSpace["y"] += direction["y"]
			#check whether to keep adding spaces to flip or to stop
			while currentSpace == oppositeSpace:
				tilesToFlipList.append([currentSpace])
				currentSpace["x"] += direction["x"]
				currentSpace["y"] += direction["y"]
		return tilesToFlipList