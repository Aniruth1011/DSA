class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0 and obstacleGrid[i][j]==0 :
                    dp[i][j] =1
                else:
                    if obstacleGrid[i][j]==1:
                        dp[i][j] = 0
                        continue
                    if i==0 and j!=0:
                        if obstacleGrid[i][j-1]==0:
                            dp[i][j] = dp[i][j-1]
                        else:
                            pass
                    elif i!=0 and j==0:
                        if obstacleGrid[i-1][j]==0:
                            dp[i][j] = dp[i-1][j]
                        else:
                            pass
                    elif i!=0 and j!=0:
                        if obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] == 0:
                            if i!=0 and j!=0:
                                dp[i][j]=dp[i-1][j] + dp[i][j-1]
                            elif i==0:
                                dp[i][j] = dp[i][j-1]
                            elif j==0:
                                dp[i][j] = dp[i-1][j]
                        elif obstacleGrid[i-1][j]==1:
                            dp[i][j]= dp[i][j-1]
                        else:
                            dp[i][j]=dp[i-1][j] 
            print(dp[i])
        return dp[-1][-1]