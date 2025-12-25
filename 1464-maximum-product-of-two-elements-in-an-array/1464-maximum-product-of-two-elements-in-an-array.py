class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        heapq.heapify(nums)
        num1 , num2 = heapq.nlargest(2 , nums)
        return (num1 - 1) * (num2- 1)
