class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n==4:
            if sum(nums) == target:
                return [nums]
        li = []
        nums = sorted(nums)
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            e1 = nums[i]
            rem_sum1 = target - e1
            for j in range(i+1 , n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                e2 = nums[j]
                if i == j:
                    continue
                rem_sum2 = rem_sum1 - e2 
                l = j+1
                r = n-1
                while (l<r):
                    e3 = nums[l]
                    e4 = nums[r]
                    s = e3 + e4 
                    if s>rem_sum2:
                        r-=1 
                    elif s<rem_sum2:
                        l+=1 
                    else:
                        li.append([e1 , e2 , e3 , e4])
                        l+=1
                        r-=1
                        while (l<r) and (nums[l] == nums[l-1]):
                            l+=1
                        while (l<r) and (nums[r] == nums[r+1]):
                            r-=1
        return li
        