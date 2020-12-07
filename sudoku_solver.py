def sudoku_solver(board):
	"""
	linear solves the board checking at each step
	of board is still valid, uses backtracking
	to slove the board
	param: board
	return: a completed board
	"""
	empty_space = find_next_empty(board)

	if empty_space:
		row, col = empty_space
	else:
		return True;

	for i in range (1,10):
		if valid_num(board,(row,col),i):
			board[row][col] = i

			if sudoku_solver(board):
				return True

			board[row][col] = 0

	return False


def find_next_empty(board):
	"""
	Linear search that finds a 
	'0' (empty space) meaing the board
	is not compelte
	param: board
	return: empty position
	"""
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j)

def valid_num(board,pos,num):
	"""
	param: board,position to check, number filled in
	return: true or false
	"""
	# Check if col is valid with the new num
	for i in range(0,8):
		if(board[i][pos[1]]==num and pos[1] != i):
			return False
	# Check if row is vlaid with the new num
	for j in range(0,8):
		if(board[pos[0]][j]==num and pos[1] != j):
			return False
	# Check if box is still valid with new num
	box_row = pos[0]//3
	box_col = pos[1]//3
	for i in range(box_row*3, box_row*3 + 3):
		for j in range(box_col*3, box_col*3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True



	return None

def print_board(board):
	"""
	prints the board
	:param : 2d List of ints
	:return: None
	"""
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("----------------------------")
		for j in range(len(board[0])):
			if j % 3 == 0:
				print(" ║ ",end="")

			if j == 8:
				print(board[i][j], end="\n")
			else:
				print(str(board[i][j]) + " ", end="")


board = [[6, 0, 0, 0, 0, 3, 0, 0, 1],
[0, 9, 0, 0, 0, 0, 0, 0, 3],
[4, 0, 3, 0, 0, 0, 6, 0, 0],
[0, 0, 0, 5, 9, 0, 2, 0, 6],
[0, 0, 0, 1, 0, 4, 0, 5, 0],
[9, 0, 0, 0, 0, 6, 0, 0, 0],
[0, 0, 0, 4, 3, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 8, 0, 0, 0],
[0, 7, 0, 0, 0, 9, 0, 0, 0]]

def main(board):
	sudoku_solver(board)
	print_board(board)

main(board)