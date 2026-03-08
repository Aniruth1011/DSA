from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int: 
        counter = Counter(nums)
        dp = [0 for i in range(max(nums)+1)]
        for num in counter:
            dp[num] = num * counter[num] 
        prev2 = 0 
        prev1 = 0 
        for val in dp: 
            curr = max(prev1, prev2 + val)
            prev2 = prev1 
            prev1 = curr 
        return prev1            
        
