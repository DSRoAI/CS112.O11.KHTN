# Function to check if there is a square with all four corners filled in the left-up position
def check_left_up(board, i, j):
    left_up = board[i][j] + board[i - 1][j] + board[i - 1][j - 1] + board[i][j - 1]
    return left_up == 4

# Function to check if there is a square with all four corners filled in the left-down position
def check_left_down(board, i, j):
    left_down = board[i][j] + board[i + 1][j] + board[i + 1][j - 1] + board[i][j - 1]
    return left_down == 4

# Function to check if there is a square with all four corners filled in the right-up position
def check_right_up(board, i, j):
    right_up = board[i][j] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j + 1]
    return right_up == 4

# Function to check if there is a square with all four corners filled in the right-down position
def check_right_down(board, i, j):
    right_down = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i][j + 1]
    return right_down == 4

# Input the dimensions of the board and the number of filled cells
n, m, k = map(int, input().split())
# Initialize the board with zeros
board = [[0] * 1000 for _ in range(1000)]

# Loop through the filled cells
for idx in range(k):
    # Input the coordinates of the filled cell
    x, y = map(int, input().split())
    # Mark the cell as filled
    board[x][y] = 1

    # Check for special cases where a square is completed
    if x == 1 and y == 1:
        if check_right_down(board, x, y):
            print(idx + 1)
            break
        continue

    if x == 1 and y == m:
        if check_left_down(board, x, y):
            print(idx + 1)
            break
        continue

    if x == n and y == 1:
        if check_right_up(board, x, y):
            print(idx + 1)
            break
        continue

    if x == n and y == m:
        if check_left_up(board, x, y):
            print(idx + 1)
            break
        continue

    # Check for border cases and corners
    if x == 1:
        if check_left_down(board, x, y) or check_right_down(board, x, y):
            print(idx + 1)
            break
        continue

    if y == 1:
        if check_right_up(board, x, y) or check_right_down(board, x, y):
            print(idx + 1)
            break
        continue

    if x == n:
        if check_right_up(board, x, y) or check_left_up(board, x, y):
            print(idx + 1)
            break
        continue

    if y == m:
        if check_left_up(board, x, y) or check_left_down(board, x, y):
            print(idx + 1)
            break
        continue

    # Check for squares in other positions
    if (
        check_left_up(board, x, y)
        or check_left_down(board, x, y)
        or check_right_up(board, x, y)
        or check_right_down(board, x, y)
    ):
        print(idx + 1)
        break
else:
    # If no square is completed, print 0
    print(0)
