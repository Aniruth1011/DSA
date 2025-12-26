class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            smallest = min(nums)
            smallest_index = nums.index(smallest)
            nums[smallest_index]*=multiplier 
        
        return nums