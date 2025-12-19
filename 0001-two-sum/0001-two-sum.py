class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for i in range(len(nums)):
            req = target - nums[i]
            if req in dic:
                return [i , nums.index(req)]
            
            dic[nums[i]] = req 