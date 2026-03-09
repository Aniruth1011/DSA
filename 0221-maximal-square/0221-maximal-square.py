class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        if m==1 and n==1:
            return int(matrix[0][0])
        dp = [[0 for i in range(n)] for j in range(m)]
        longest_len = 0
        for i in range(m):
            for j in range(n):
                if i==0:
                    dp[i][j] = int(matrix[i][j])
                elif j==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j]=="1":
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                longest_len = max(longest_len , dp[i][j])
        return longest_len * longest_len



