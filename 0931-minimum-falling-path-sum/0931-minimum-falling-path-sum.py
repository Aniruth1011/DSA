class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for x in range(m):
            for y in range(n):
                if x==0:
                    dp[x][y] = matrix[x][y]
                if y==0:
                    dp[x][y] = matrix[x][y] + min(dp[x-1][y] , dp[x-1][y+1])
                elif y==n-1:
                    dp[x][y] = matrix[x][y] + min(dp[x-1][y] , dp[x-1][y-1])
                else:
                    dp[x][y] = matrix[x][y] + min(dp[x-1][y-1] , dp[x-1][y] , dp[x-1][y+1]) 
        return min(dp[-1])
