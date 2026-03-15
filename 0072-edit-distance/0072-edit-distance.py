class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1) , len(word2)
        if m == 0 and n==0:
            return 0 
        elif m==0 or n==0:
            return max(m,n)
        rows_word, cols_word = (word1, word2) if m >= n else (word2, word1)
        rows, cols = len(rows_word), len(cols_word)     
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)] 
        # if word1[0] != word2[0]:
        #     dp[0][0] = 1 
        # for i in range(1 , cols):
        #     if cols_word[i] == rows_word[0]:
        #         dp[0][i] = dp[0][i-1]
        #     else:
        #         dp[0][i] = dp[0][i-1] + 1
        # for i in range(1 , rows):
        #     if rows_word[i] == cols_word[0]:
        #         dp[i][0] = dp[i-1][0]
        #     else:
        #         dp[i][0] = dp[i-1][0] + 1
        for i in range(1, rows+1):
            dp[i][0] = i
        for j in range(1, cols+1):
            dp[0][j] = j        
        for i in range(1 , rows+1):
            for j in range(1 , cols+1):
                if rows_word[i-1] == cols_word[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(dp[i-1][j-1] , dp[i][j-1] , dp[i-1][j]) + 1 
        
        return dp[rows][cols]
                    
