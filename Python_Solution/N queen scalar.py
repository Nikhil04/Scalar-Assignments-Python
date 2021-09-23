class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = [['.']*A for _ in range(A)]

        def check(x,y,board):
            for i in range(A):
                for j in range(A):
                    if board[i][j]=='Q':
                        if i==x or j==y or (x-y)==(i-j) or (x+y)==(i+j):
                            return False
            return True
        
        def solve(board,qn,ans):
            if qn==A:
                to_append = [''.join(sa) for sa in board]
                ans.append(to_append)
                return
        
            for c in range(A):
                if check(qn,c,board):
                    board[qn][c] = 'Q'
                    solve(board,qn+1,ans)
                    board[qn][c] = '.'
        
        ans = list()
        solve(board,0,ans)
        print(ans)