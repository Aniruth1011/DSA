class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        reverse_array = sorted(nums )
        n = len(nums)
        res = []
        for i in range(n//2):
            res.append(reverse_array[(2*i)+1])
            res.append(reverse_array[2*i])
        
        return res