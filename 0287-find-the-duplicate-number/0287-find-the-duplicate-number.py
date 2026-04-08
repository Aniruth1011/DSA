class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        counts = set() 
        for i in nums:
            if i in counts:
                return i 
            counts.add(i)