class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0 
        return sum(nums[::2])