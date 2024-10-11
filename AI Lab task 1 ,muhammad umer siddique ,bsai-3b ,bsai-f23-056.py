def game_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def game_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'x'
    while True:
        game_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))
        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move, try again.")
            continue
        board[row][col] = current_player
        winner = game_winner(board)
        if winner:
            game_board(board)
            print(f"Player {winner} wins!")
            break
        if is_full(board):
            game_board(board)
            print("It's a tie:")
            break
        current_player = 'o' if current_player == 'x' else 'x'

