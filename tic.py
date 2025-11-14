# --- Tic Tac Toe (+1 vs -1, positions 1–9) ---

def print_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val == 0:
                print("   ", end=" ")  # show empty space
            else:
                print(f"{val:>3}", end=" ")
        print()
    print()


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if abs(sum(board[i])) == 3:  # row
            return True
        if abs(board[0][i] + board[1][i] + board[2][i]) == 3:  # column
            return True

    # Check diagonals
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return True
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return True

    return False


# Initialize empty board (0 means empty)
board = [[0 for _ in range(3)] for _ in range(3)]
occupied = set()

print("Welcome to Tic Tac Toe (+1 vs -1)!")
print("Positions are numbered 1–9 as follows:\n")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")

turn = 1  # +1 starts

for move in range(9):
    player = "+1" if turn == 1 else "-1"
    print(f"\nPlayer {player}'s turn.")

    try:
        pos = int(input("Enter position (1–9): "))
        if pos < 1 or pos > 9:
            print("Invalid position. Choose between 1 and 9.")
            continue
        if pos in occupied:
            print("That position is already taken. Try again.")
            continue
    except ValueError:
        print("Invalid input. Enter a number between 1–9.")
        continue

    # Convert position to matrix indices
    row, col = (pos - 1) // 3, (pos - 1) % 3
    board[row][col] = turn
    occupied.add(pos)

    print_board(board)

    # Check if someone won
    if check_winner(board):
        print(f"🎉 Player {player} wins!")
        break

    # Switch turn
    turn *= -1

else:
    print("It's a draw!")
