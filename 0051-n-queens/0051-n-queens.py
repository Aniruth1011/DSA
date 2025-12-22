class Solution: 
    def isok(self , board , r , c , n):
        for i in range(n):
            if board[i][c] == "Q":
                return False 
            if board[r][i] == "Q":
                return False 
        i, j = r, c
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = r, c
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        i, j = r, c
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1

        i, j = r, c
        while i < n and j < n:
            if board[i][j] == "Q":
                return False
            i += 1
            j += 1

        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)] 
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if self.isok(board, row, col, n):
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."  

        backtrack(0)
        return res 