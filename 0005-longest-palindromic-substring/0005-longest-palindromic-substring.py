class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        elif n==1:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True 
        max_len = 1 
        start = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                l = 2 
                if l>max_len:
                    max_len = l 
                    start = i
        for l in range(3 , n+1):
            for i in range(n-l+1):
                if s[i] == s[i+l-1] and dp[i+1][i+l-2]:
                    dp[i][i+l-1] = True 
                    if l > max_len:
                        max_len = l 
                        start = i 
        return s[start:start+max_len]
        