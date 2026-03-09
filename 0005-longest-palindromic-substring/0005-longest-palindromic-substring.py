class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True 
            start = i 
            max_len = 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                start = i 
                max_len = 2
        for l in range(3, n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_len = l
        return s[start:start+max_len]