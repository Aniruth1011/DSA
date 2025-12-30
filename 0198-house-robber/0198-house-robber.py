class Solution:
    def rob(self, nums: List[int]) -> int:

        i_1 , i_2 = 0 , 0
        for num in nums:
            i_2, i_1 = i_1 , max(i_1 , i_2 + num)
        return max(i_2 , i_1)