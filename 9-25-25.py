board = ['_','_','_','_','_','_','_','_','_']

WIN = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(board):
    for a,b,c in WIN:
        if board[a] != '_' and board[a] == board[b] == board[c]:
            return board[a]
    return 'Draw' if '_' not in b else None 

def display(board):
    print('')