#tic tac toe
# Tic-Tac-Toe Game in Python (2 Players - CLI)

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

            if board[row][col] != ' ':
                print("Cell already taken! Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins! 🎉")
                break

            if is_full(board):
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        except (ValueError, IndexError):
            print("Invalid input! Enter numbers from 1 to 3.")


# Run the game
if __name__ == "__main__":
    play_game()
