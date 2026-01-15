from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        num_0 = counter[0]
        num_1 = counter[1]
        num_2 = counter[2]
        print(num_0 , num_1 , num_2)
        nums[:num_0] = [0] * num_0 
        nums[num_0:num_0+num_1] = [1] * num_1 
        nums[num_0+num_1:num_0+num_1 + num_2] = [2] * num_2

