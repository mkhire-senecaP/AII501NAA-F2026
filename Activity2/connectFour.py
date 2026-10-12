import numpy as np
ROWS = 6
COLS = 7
def create_board():
    board = np.zeros((ROWS,COLS),dtype=int)
    return board


#print(board)

def is_valid_col(board,col):
    if int(board[0][col]) == 0:
        return True
    else:
        return False
    
def drop_piece(board,col,player):
    if is_valid_col(board,col):
        for r in range(len(board)-1,-1,-1):
            if board[r][col] == 0:
                board[r][col] = player
                return True
    else:
        print("Column Full. Try another column")
        return False

def input_col(board,player):
    player_input = 0
    while player_input >= 8 or player_input <=0:
        try:
            col = int(input("Player " + str(player) + " choose a column (1-7): "))
        except ValueError:
            print("integer between 1 and 7, inclusive")
        if col < 1 or col > 7:
            print("Input between 1 and 7")
            continue
        if drop_piece(board,col - 1,player):
            print(board)
            return True
        print("Column Full. Try another column")
           
        
def current_player(state):
    return 1 if np.sum(state == 1) == np.sum(state == 2) else 2

def legal_moves(board):
    return [col for col in range(COLS) if is_valid_col(board, col)]

def game_over(board):
    return check_win(board) is not None or len(legal_moves(board)) == 0

def check_win(board):
    for r in range(len(board)):
        for c in range(len(board[r])-3):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] :
                    print("Player ", str(board[r][c])[0]," wins!")
                    return True
# vertical check
    for r in range(len(board) - 3):
        for c in range(len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    print("Player ", str(board[r][c])[0]," wins!")
                    return True
# check positive diagonal
    for r in range(0,len(board) - 3):
        for c in range(0,len(board[r]) - 3):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    print("Player ", str(board[r][c])[0]," wins!")
                    return True
# check negative diagonal
    for r in range(len(board)-3):
        for c in range(3, len(board[r])):
            if board[r][c] == 1 or board[r][c] == 2:
                if board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    print(print("Player ", str(board[r][c])[0]," wins!"))
                    return True                         

def play(board,player_turn=1):
    board = create_board()
    print(board)
    while True:
        input_col(board,player_turn)
        winner = check_win(board)
        if winner:
            print("Player", winner, "wins")
        if not legal_moves(board):
            print("Draw")
            break
        player_turn = 3 - player_turn
"""       
        if player_turn == 1:
            if input_col(board,1):
                player_turn = 2
                print(type(board), board)
                if(check_win(board)):
                    break
            else:
                player_turn = 1
        if player_turn == 2:
            if input_col(board,2):
                player_turn = 1
                if(check_win(board)):
                    break
            else:
                player_turn = 2
"""


if __name__ == "__main__":
    play(create_board(),1)