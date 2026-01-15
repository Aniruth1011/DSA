class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        l = 0 
        longest = 0 
        nums = set(nums)
        for num in nums:
            if num -1 not in nums:
                copy = num 
                l = 0
                while copy in nums:
                    copy+=1 
                    l+=1 
                longest = max(longest , l)
        
        return longest 
