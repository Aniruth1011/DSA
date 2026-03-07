class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo = {}
        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     if n==0:
        #         return cost[0]
        #     elif n==1:
        #         return cost[1]
        #     else:
        #         memo[n] =  cost[n] + min(dp(n-1), dp(n-2)) 
        #         return memo[n]
        # n = len(cost)
        # return min(dp(n-1) , dp(n-2))
        n = len(cost)
        if n==1:
            return cost[0]
        elif n==2:
            return min(cost[0] , cost[1])
        dp = [0 for i in range(n+1)]   
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(cost[i-1] + dp[i-1] , cost[i-2] + dp[i-2])
        return dp[n]