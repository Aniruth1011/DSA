class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        sorted_list = sorted(nums)

        k_largest = sorted_list[-k:]
        res = []
        c = 0 
        from collections import Counter 
        counter = Counter(k_largest)
        for i in nums:
            if counter[i] > 0:
                res.append(i)
                counter[i]-=1
                if len(res) == k:
                    break
        return res 
