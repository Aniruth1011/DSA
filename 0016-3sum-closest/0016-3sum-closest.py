class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:


        n = len(nums)
        if n==3:
            return sum(nums) 
        nums = sorted(nums)
        most_closest = inf
        triplet_sum = 0
        for i in range(n-2):
            el = nums[i]
            l = i+1
            r = n-1
            while (l<r):
                el1 = nums[l]
                el2 = nums[r]
                s = el1 + el2 + el
                diff = abs(s - target) 
                sum_ = el1 + el2 + el
                if most_closest > diff: 
                    most_closest = diff 
                    triplet_sum = el + el1 + el2 
                
                if s>target:
                    r-=1
                elif s<target:
                    l+=1
                else:
                    return target 
        
        return triplet_sum
            
                