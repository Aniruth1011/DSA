class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_sum = nums[0] + nums[1] + nums[2]
        most_closest = abs(best_sum - target)
        for idx in range(n-2):
            num1 = nums[idx]
            left = idx+1
            right = n-1
            while (left < right):
                num2 = nums[left]
                num3 = nums[right]
                total_sum = num1 + num2 + num3
                if abs( total_sum - target) < most_closest:
                    most_closest = abs(total_sum - target)
                    best_sum = total_sum
                if (num1+num2+num3) == target:
                    return total_sum
                elif (total_sum) < target:
                    left+=1 
                else:
                    right-=1
        return best_sum 
