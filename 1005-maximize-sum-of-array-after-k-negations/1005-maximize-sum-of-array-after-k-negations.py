class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            min_val_index = nums.index(min(nums))
            nums[min_val_index] *= (-1)
        return sum(nums)
