class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        dp = [[0 for i in range(n)] for j in range(m)]
        #return dp_fun(m-1 , n-1)
        for x in range(m):
            for y in range(n):
                if x==0 and y==0:
                    dp[x][y] = 0 
                elif x==0 and y==1:
                    dp[x][y] = 1
                elif x==1 and y==0:
                    dp[x][y] = 1
                else:
                    if (x==0) :
                        dp[x][y] = dp[x][y-1]
                    elif (y==0) :
                        dp[x][y] = dp[x-1][y]
                    else:
                        dp[x][y] = dp[x][y-1] + dp[x-1][y] 
                # print(x,y,dp[x][y])    

        for i in range(m):
            print(dp[i])

        return dp[m-1][n-1]
