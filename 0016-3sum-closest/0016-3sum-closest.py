class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_sum = nums[0] + nums[1] + nums[2]
        most_closest = abs(best_sum - target)
        for idx , num1 in enumerate(nums):
            num1 = nums[idx]
            left = idx+1
            right = n-1
            while (left < right):
                num2 = nums[left]
                num3 = nums[right]
                if abs(num1 + num2 + num3 - target) < most_closest:
                    most_closest = abs(num1 + num2 + num3 - target)
                    best_sum = num1 + num2 + num3
                if (num1+num2+num3) == target:
                    return num1 + num2 + num3
                elif (num1+num2+num3) < target:
                    left+=1 
                else:
                    right-=1
        return best_sum 
