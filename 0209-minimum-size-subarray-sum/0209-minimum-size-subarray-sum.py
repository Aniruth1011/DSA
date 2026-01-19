class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        r = 0 
        n = len(nums)
        s = 0
        min_len = float('inf')
        while r < n:
            s+= nums[r]
            if s >=target:
                min_len = min(min_len , r - l + 1)
                while (s>=target) and (l <= r):
                    min_len = min(min_len , r - l + 1)
                    s-=nums[l]
                    l+=1 
            r+=1 
        
        if min_len == float('inf'):
            return 0 
        return min_len 
