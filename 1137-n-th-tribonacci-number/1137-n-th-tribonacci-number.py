class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0 
        elif n==1 or n==2:
            return 1
        memo = [0 for i in range(n+1)]
        memo[0] = 0 
        memo[1] = 1
        memo[2] = 1 
        for i in range(3 , n+1):
            memo[i] = memo[i-3] + memo[i-1] + memo[i-2] 
        
        return memo[n]