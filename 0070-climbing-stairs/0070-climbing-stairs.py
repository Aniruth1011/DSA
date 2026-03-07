class Solution:
    def climbStairs(self, n: int) -> int: 
        if n<=2:
            return n
        opt = [0 for i in range(n)]
        opt[0] = 1
        opt[1] = 2
        for i in range(2,n):
            opt[i] = opt[i-1] + opt[i-2]
        return opt[n-1]
        