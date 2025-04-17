def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True

    result = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            result = solve_n_queens(board, row + 1, n) or result
            board[row][col] = '.'  # Backtrack
    return result


def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    # print(board)
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")


# Example: Solve for N = 4
n_queens(4)
