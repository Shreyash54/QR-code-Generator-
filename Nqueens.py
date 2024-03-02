
def print_solution(board):
    for row in board:
        print ("".join(map(str,row)))
    print("\n")

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(n):
        if board[i][col]==1:
            return False

        # Check if there is a queen in the same column
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j - 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j + 1

    return True



def solve_nqueens_until(board,row,n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            solve_nqueens_until(board,row+1,n)
            board[row][col]=0


def solve_nqueens():
    n =int(input("enter no.of queens to backtrack:"))
    board = [[0] * n for _ in range(n)]
    solve_nqueens_until(board,0,n)

solve_nqueens()
