class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []
        for idx1 in range(n-3):
            if idx1>0 and nums[idx1] == nums[idx1-1]:
                continue 
            num1 = nums[idx1]
            for idx2 in range(idx1+1 , n-2):
                if idx2 > idx1+1 and nums[idx2] == nums[idx2-1]:
                    continue
                num2 = nums[idx2]
                left = idx2+1
                right = n-1
                while (left < right):
                    current_sum = num1 + num2 + nums[left] + nums[right]
                    if (current_sum == target):
                        results.append([num1 , num2 , nums[left] , nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        while right>left and nums[right] == nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif (current_sum < target):
                        left+=1
                    else:
                        right-=1
        return results 