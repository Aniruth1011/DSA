class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m , n=  len(matrix) , len(matrix[0])
        dp = matrix[0][:]
        for i in range(1 , m):
            prev_row = dp[:]
            for j in range(n):
                if j==0:
                    dp[j] = matrix[i][j] +  min(prev_row[j] , prev_row[j+1])
                elif j == n-1:
                    dp[j] = matrix[i][j] + min(prev_row[j] , prev_row[j-1])
                else:
                    dp[j] = matrix[i][j] + min(prev_row[j] , prev_row[j+1] , prev_row[j-1]) 
            print(dp)
        return min(dp)

        # 2 1 3 
        # 6 5 4 
        # 7 8 9  

        #


        # m , n = len(matrix) , len(matrix[0])
        # dp = [0 for i in range(n)]
        # for x in range(m):
        #     prev_row = dp[:]
        #     for y in range(n):
        #         if x==0:
        #             dp[y] = matrix[x][y]
        #         elif y==0:
        #             dp[y] = matrix[x][y] + min(prev_row[y] , prev_row[y+1])
        #         elif y==n-1:
        #             dp[y] = matrix[x][y] + min(prev_row[y] , prev_row[y-1])
        #         else:
        #             dp[y] = matrix[x][y] + min(prev_row[y] , prev_row[y-1] , prev_row[y+1])
        return min(dp)
        # dp = [[0 for i in range(n)] for j in range(m)]
        # for x in range(m):
        #     for y in range(n):
        #         if x==0:
        #             dp[x][y] = matrix[x][y]
        #         elif y==0:
        #             dp[x][y] = matrix[x][y] + min(dp[x-1][y] , dp[x-1][y+1])
        #         elif y==n-1:
        #             dp[x][y] = matrix[x][y] + min(dp[x-1][y] , dp[x-1][y-1])
        #         else:
        #             dp[x][y] = matrix[x][y] + min(dp[x-1][y-1] , dp[x-1][y] , dp[x-1][y+1]) 
        # return min(dp[-1])
