class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        for idx , num1 in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            target = -num1 
            left = idx+1
            right = n-1 
            while (left < right):
                num2 = nums[left]
                num3 = nums[right] 
                if (num2 + num3) == target:
                    answer.append([num1 , num2 , num3])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif (num2 + num3) > target:
                    right-=1 
                else:
                    left+=1 
        return answer 