# Nqueen
def safe(row,col,board,A):
    i=row-1
    while(i>=0):
        if board[i][col]=="Q":
            return False
        i-=1
    i=row-1
    j=col-1
    while(i>=0 and j>=0):
        if board[i][j]=="Q":
            return False
        i-=1
        j-=1
    i=row-1
    j=col+1
    while(i>=0 and j<A):
        if board[i][j]=="Q":
            return False
        i-=1
        j+=1
    return True
    
def helper(board,row,ans,A):
    if(row==A):
        to_append = [''.join(sa) for sa in board]
        ans.append(to_append)
        return
    for col in range(A):
        if safe(row,col,board,A) is True:
            board[row][col]="Q"
            helper(board,row+1,ans,A)
            board[row][col]="."
    return 
def solveNQueens(A):
    ans=[]
    board=[["." for j in range(A)] for i in range(A)]
    helper(board,0,ans,A)
    return ans

print(solveNQueens(4))
    
