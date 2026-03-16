class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 0 
        for x in arr:
            dp[x] = dp.get(x - difference , 0) +1 
            res = max(dp[x] , res)
        return res 
        