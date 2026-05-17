from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for num , ct in dic.items():
            if ct==1:
                return num