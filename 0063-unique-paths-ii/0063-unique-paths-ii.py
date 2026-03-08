class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j>0:
                    dp[j] += dp[j-1]
        return dp[-1]


        # dp = [[0 for i in range(n)] for j in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0 
        #         elif i==0 and j==0:
        #             dp[i][j] = 1
        #         else:
        #             if i>0:
        #                 up = dp[i-1][j]
        #             else:
        #                 up = 0 
        #             if j>0:
        #                 left = dp[i][j-1]
        #             else:
        #                 left = 0 
        #             dp[i][j] = up + left 
        # return dp[-1][-1]