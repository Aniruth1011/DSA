class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 0
        n = len(nums)
        seen = set()
        while (r<n):
            if r-l > k:
                seen.remove(nums[l]) 
                l+=1

            if nums[r] in seen:
                return True 
        
            seen.add(nums[r])

            r+=1
        return False 

"""
[012325]
l = 0, r=0 
l = 0, r=1
l = 0, r=2
l = 0, r=3
l = 0, r=4 
l = 1, r=4 
l = 1 , r = 5
l = 2 , r =5
"""