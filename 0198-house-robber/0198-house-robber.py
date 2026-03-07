class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n==2:
            return max(nums)
        def dp(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            if n==0:
                return nums[n]
            if n==1:
                return max(nums[0] , nums[1])
            else:
                memo[n] = max(nums[n] + dp(n-2) , dp(n-1)) 
                return memo[n]
        return dp(n-1)