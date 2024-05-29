import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = player
                break
            else:
                print("Cell is already taken. Choose another move.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board, player):
    # Try to find a winning move
    for move in range(9):
        row, col = divmod(move, 3)
        if board[row][col] not in ['X', 'O']:
            board[row][col] = player
            if check_winner(board, player):
                return
            board[row][col] = str(move + 1)

    # Try to block the opponent's winning move
    opponent = 'X' if player == 'O' else 'O'
    for move in range(9):
        row, col = divmod(move, 3)
        if board[row][col] not in ['X', 'O']:
            board[row][col] = opponent
            if check_winner(board, opponent):
                board[row][col] = player
                return
            board[row][col] = str(move + 1)
    
    # Otherwise, choose a random valid move
    valid_moves = [move for move in range(9) if board[move // 3][move % 3] not in ['X', 'O']]
    move = random.choice(valid_moves)
    board[move // 3][move % 3] = player

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = 'X'
    
    while True:
        print_board(board)
        if current_player == 'X':
            player_move(board, current_player)
        else:
            ai_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
