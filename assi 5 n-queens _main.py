# N-Queens problem solution using backtracking

N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    # Check the column
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the lower-left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solveNQUtil(board, col):
    # Base case: if all queens are placed
    if col >= N:
        return True
    
    # Try to place a queen in each row of the current column
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1
            
            # Recur for the next column
            if solveNQUtil(board, col + 1) == True:
                return True
            
            # If placing the queen in the current position doesn't lead to a solution, backtrack
            board[i][col] = 0
    
    return False

def solveNQ():
    board = [[0, 0, 0, 0,],
             [0, 0, 0, 0,],
             [0, 0, 0, 0,],
             [0, 0, 0, 0,]]
    
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False
    
    printSolution(board)
    return True

solveNQ()