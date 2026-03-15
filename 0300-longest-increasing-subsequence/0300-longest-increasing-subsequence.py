class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [1 for i in range(m)]
        for i in range(m):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , dp[j] + 1) 
        return max(dp)