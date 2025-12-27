class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0 
        max_index = 0 
        n = len(nums)
        for idx in range(n):
            if idx > max_index:
                return False 
            
            max_index = max(max_index , idx + nums[idx])

            if max_index>=n-1:
                return True 
            
        return True