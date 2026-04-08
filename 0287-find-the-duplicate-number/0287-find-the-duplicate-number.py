class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [0 for i in range(n)] #* n 
        for i in nums:
            counts[i-1] = counts[i-1] + 1
            if counts[i-1] == 2:
                return i