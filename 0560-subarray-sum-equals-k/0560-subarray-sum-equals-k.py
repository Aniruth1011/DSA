from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        s = 0
        res = 0
        for i in nums:
            s+=i 
            res+=counter[s-k]
            counter[s]+=1
        return res 

            