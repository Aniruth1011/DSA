class Solution:
    def totalNQueens(self, n: int) -> int:
        def boardisok(x , y , board):
            n = len(board)
            m  = n
            for i in range(n):
                if board[x][i] == "Q" or board[i][y] == "Q":
                    return False 
            a = x
            b = y 
            while ((0<=a) and (a<n)) and ( (0<=b) and (b<m) ):
                if board[a][b] == "Q":
                    return False
                a+=1
                b+=1 
            a = x
            b = y 
            while ((0<=a) and (a<n)) and ( (0<=b) and (b<m) ):
                if board[a][b] == "Q":
                    return False
                a+=1
                b-=1 
            a = x
            b = y 
            while ((0<=a) and (a<n)) and ( (0<=b) and (b<m) ):
                if board[a][b] == "Q":
                    return False
                a-=1
                b-=1 
            a = x
            b = y 
            while ((0<=a) and (a<n)) and ( (0<=b) and (b<m) ):
                if board[a][b] == "Q":
                    return False
                a-=1
                b+=1 
            return True
        
        result = []
        board = [["." for i in range(n)] for j in range(n)]

        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0
                for col in range(n):
                    if boardisok(row , col , board):
                        board[row][col] = "Q"
                        count += backtrack(row+1)
                        board[row][col] = "."
                return count
        return backtrack(0)
