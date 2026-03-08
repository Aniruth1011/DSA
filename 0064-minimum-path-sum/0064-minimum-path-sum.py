class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        dp =[0 for i in range(n)]
        for x in range(m):
            for y in range(n):
                if x==0 and y==0:
                    dp[y] = grid[x][y]
                elif x==0:
                    dp[y] = grid[x][y] + dp[y-1]
                elif y==0:
                    dp[y] = grid[x][y] + dp[y]
                else:
                    dp[y] = grid[x][y] + min(dp[y-1] , dp[y])
                
        return dp[n-1]
