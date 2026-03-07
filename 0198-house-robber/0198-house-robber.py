class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}
        # n = len(nums)
        # if n==2:
        #     return max(nums)
        # def dp(n):
        #     if n in memo:
        #         return memo[n]
        #     if n < 0:
        #         return 0
        #     if n==0:
        #         return nums[n]
        #     if n==1:
        #         return max(nums[0] , nums[1])
        #     else:
        #         memo[n] = max(nums[n] + dp(n-2) , dp(n-1)) 
        #         return memo[n]
        # return dp(n-1)
        n = len(nums)
        if n==0:
            return 0 
        elif n==1:
            return nums[0]
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
