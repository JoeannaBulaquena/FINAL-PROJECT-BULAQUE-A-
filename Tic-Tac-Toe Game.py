def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    player_names = {players[0]: player1, players[1]: player2}

    for _ in range(9):
        print_board(board)
        current_player = players[turn % 2]
        print(f"{player_names[current_player]}'s turn ({current_player})")
        row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"{player_names[current_player]} wins!")
                return
            turn += 1
        else:
            print("Cell already taken, try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()