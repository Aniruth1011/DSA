class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        longest = 0 
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1:
                longest = 1
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                longest = 1

        for i in range(1 , m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1]) 
                    longest = max(longest , dp[i][j])
        
        return longest**2




        """
        1 0 1 0 0 
        1 0 1 1 1 
        1 1 1 2 2

        """



























        # m , n = len(matrix) , len(matrix[0])
        # dp = [0 for i in range(n)]
        # longest_len = 0
        # for i in range(m):
        #     prev_diag = 0
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[j] = int(matrix[i][j])
        #         else:
        #             temporary = dp[j]
        #             if matrix[i][j]=="1":
        #                 dp[j] = min(dp[j] , dp[j-1] , prev_diag) + 1
        #             longest_len = max(longest_len , dp[j])
        #             prev_diag = temporary 
        # return longest_len 

        # if m==1 and n==1:
        #     return int(matrix[0][0])
        # dp = [[0 for i in range(n)] for j in range(m)]
        # longest_len = 0
        # for i in range(m):
        #     for j in range(n):
        #         if i==0:
        #             dp[i][j] = int(matrix[i][j])
        #         elif j==0:
        #             dp[i][j] = int(matrix[i][j])
        #         else:
        #             if matrix[i][j]=="1":
        #                 dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        #         longest_len = max(longest_len , dp[i][j])
        # return longest_len * longest_len



