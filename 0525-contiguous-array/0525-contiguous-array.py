class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        prefix_sum = [1 if i == 1 else -1 for i in nums]
        dic = {0 : -1}
        max_len = 0
        s = 0
        for i , num  in enumerate(prefix_sum):
            s+= num 
            if s in dic:
                max_len = max(max_len, i - dic[s])
            else:
                dic[s] = i 
        
        return max_len
