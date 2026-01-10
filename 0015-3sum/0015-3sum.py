class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = set()
        for idx , num1 in enumerate(nums):
            target = -num1 
            left = idx+1
            right = n-1 
            while (left < right):
                num2 = nums[left]
                num3 = nums[right] 
                if (num2 + num3) == target:
                    answer.add((num1 , num2 , num3))
                    left+=1
                    right-=1
                elif (num2 + num3) > target:
                    right-=1 
                else:
                    left+=1 
        return list(answer)
