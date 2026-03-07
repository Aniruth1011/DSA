class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n==0:
                return cost[0]
            elif n==1:
                return cost[1]
            else:
                memo[n] =  cost[n] + min(dp(n-1), dp(n-2)) 
                return memo[n]
        n = len(cost)
        return min(dp(n-1) , dp(n-2))
        
        # n = len(cost)
        # if n<=3:
        #     return cost[0] 
        # prev_2 = cost[2]
        # prev_1 = cost[1]
        # min_cost1 = 0
        # for i in range(3,n):
        #     min_cost1 = min_cost1 + min(prev_1 , prev_2)
        #     prev_1 , prev_2 = cost[i] , prev_1 
        # prev_2 = cost[1]
        # prev_1 = cost[0]
        # min_cost = 0
        # for i in range(2,n):
        #     min_cost = min_cost + min(prev_1 , prev_2)
        #     prev_1 , prev_2 = cost[i] , prev_1
        # print(min_cost,min_cost1)
        # return min(min_cost,min_cost1)
        