# Tic-Tac-Toe Game

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move as 'row,col' (e.g., 1,2): ")
        try:
            row, col = map(int, move.split(','))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Cell is occupied or out of bounds. Try again.")
        except:
            print("Invalid format. Please use 'row,col' with numbers 0, 1, or 2.")

def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! 🎉")
            break
        
        if check_draw(board):
            display_board(board)
            print("It's a draw! ")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_tic_tac_toe()
