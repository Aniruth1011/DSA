class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n==4:
            if sum(nums) == target:
                return [nums]
        li = []
        nums = sorted(nums)
        for i in range(n):
            e1 = nums[i]
            rem_sum1 = target - e1
            for j in range(i+1 , n):
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
                        if (i==j) or (i ==l) or (i ==r) or (j == l) or (j == r) or (l ==r):
                            continue
                        else:
                            if [e1 , e2 , e3 , e4] not in li:
                                li.append([e1 , e2 , e3 , e4])
                            l+=1
                            r-=1
        return li
        