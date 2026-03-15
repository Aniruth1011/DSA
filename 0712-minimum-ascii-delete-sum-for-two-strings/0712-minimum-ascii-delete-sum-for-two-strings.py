class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m , n = len(s1) , len(s2)
        if m==0 and n==0:
            return 0 
        elif m==0:
            s = 0 
            for i in s2:
                s+=ord(i)
            return s
        elif n==0:
            s=0 
            for i in s1:
                s+=ord(i)
            return s
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1 , m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]) , dp[i][j-1] + ord(s2[j-1]))
        return dp[m][n]