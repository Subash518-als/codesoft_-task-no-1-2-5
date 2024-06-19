import math

# Define constants for the players
HUMAN = -1
AI = 1

# Function to initialize the game board
def init_board():
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# Function to check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == 0

# Function to make a move
def make_move(board, row, col, player):
    board[row][col] = player

# Function to check for a winner
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if abs(sum(board[i])) == 3:
            return board[i][0]
        if abs(sum([board[j][i] for j in range(3)])) == 3:
            return board[0][i]
    
    # Check diagonals
    if abs(board[0][0] + board[1][1] + board[2][2]) == 3:
        return board[0][0]
    if abs(board[0][2] + board[1][1] + board[2][0]) == 3:
        return board[0][2]
    
    # No winner yet
    return None

# Function to check for a draw
def is_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, player):
    winner = check_winner(board)
    if winner is not None:
        return winner * player
    
    if is_draw(board):
        return 0
    
    if player == AI:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if is_valid_move(board, i, j):
                    make_move(board, i, j, AI)
                    eval = minimax(board, depth + 1, alpha, beta, HUMAN)
                    make_move(board, i, j, 0)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if is_valid_move(board, i, j):
                    make_move(board, i, j, HUMAN)
                    eval = minimax(board, depth + 1, alpha, beta, AI)
                    make_move(board, i, j, 0)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to get the best move for the AI
def get_best_move(board):
    best_val = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if is_valid_move(board, i, j):
                make_move(board, i, j, AI)
                move_val = minimax(board, 0, -math.inf, math.inf, HUMAN)
                make_move(board, i, j, 0)
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Function to print the board
def print_board(board):
    chars = {HUMAN: 'X', AI: 'O', 0: ' '}
    for row in board:
        print('|'.join([chars[cell] for cell in row]))
        print('-' * 5)

# Main function to play the game
def play_game():
    board = init_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column 0, 1, or 2 separated by a space): ").split())
                if row in range(3) and col in range(3) and is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
        make_move(board, row, col, HUMAN)
        print_board(board)
        
        if check_winner(board) == HUMAN:
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        move = get_best_move(board)
        make_move(board, move[0], move[1], AI)
        print_board(board)

        if check_winner(board) == AI:
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
