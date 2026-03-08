class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for x in range(m):
            for y in range(n):
                if x==0 and y==0:
                    dp[x][y] = grid[x][y]
                else:
                    if x==0:
                        dp[x][y] =  grid[x][y] + dp[x][y-1] 
                    elif y==0:
                        dp[x][y] =  grid[x][y] + dp[x-1][y] 
                    else:
                        dp[x][y] = grid[x][y] + min(dp[x-1][y] , dp[x][y-1])
        return dp[m-1][n-1]
