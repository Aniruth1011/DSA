class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        if n==0:
            return 0
        l = 0 
        r = 0 
        s = 0
        minlen = float('inf')
        while (r<n):
            el = nums[r]
            s+=el 

            while s>=target:
                s-=nums[l]
                minlen = min(minlen , r-l+1)
                l+=1 

            r+=1 

        if minlen == float('inf'):
            return 0
        return minlen
