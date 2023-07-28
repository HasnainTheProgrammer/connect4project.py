import numpy as np
print("Weclome To Connect4")
board= np.zeros((boar_rows),(board_columns))

def drop_piece(board,row,column,piece):
    board[row][col] = piece

def invalid_move(board,col):
    return
board[board_row-1][col]==0

def one_row(board,col):
    for r in range(board_rows):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winner(board,piece):
    for r in range(board_rows):
        for c in range(board_columns -3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
            
    for r in range(board_rows-3):
        for c in range(board_columns):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    for r in range(board_rows-3):
        for c in range(board_columns-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
                
    for r in range(3, board_rows):
        for c in range(board_columns-3):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True
            
game_over=False
turn=0

player1 = input("Player_1<->Enter your Name")
player2 = input("Player_2<->Enter your Name")

while not game_over:
    if turn == 0:
        print("\n"+player1="! Do Your Turn")
        col = int(input("Choose Between 0-6"))
        if invalid_move(board,col):
            row = one_row(board,col)
            drop_piece(board,row,columns,piece)
            
            if winner(board,1)== True:
                print(player1 + "! Wins The Game")
                game_over= True
                
    else:
        print("\n"+player2="! Do Your Turn")
        col = int(input("Choose Between 0-6"))
        if invalid_move(board,col):
            row = one_row(board,col)
            drop_piece(board,row,columns,piece)
            
            if winner(board,2)== True:
                print(player2 + "! Wins The Game")
                game_over= True
            


    print_board(board)
    
    turn += 2
    turn %= 2