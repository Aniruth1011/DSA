class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0 
        curr_sum = 0 
        for i in nums:
            curr_sum += i 
            min_val = min(min_val , curr_sum)
        return 1 - min_val 
