def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    
    i,j =row, col
    while i>=0 and j>=0:
        if board[i][j]== "Q":
            return False
        i -=1
        j -=1
    
    i,j =row, col
    while i>=0 and j<n:
        if board[i][j]== "Q":
            return False
        i -=1
        j +=1
    
    return True

def solve_n_queen(board, row, n):
    if row == n:
        print_board(board)
        return True

    result = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            result = solve_n_queen(board, row+1, n) or result
            board[row][col] = "."
    return result

def n_queen(n):
    board= [['.' for _ in range(n)] for _ in range(n)]
    print_board(board)
    if not solve_n_queen(board, 0, n):
        print("No solution exist")

n = int(input("Input Number of Queen: "))
n_queen(n)