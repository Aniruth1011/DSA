class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        max_per = 0
        for i in range(n-1 , 1 , -1):
            a , b , c = nums[i-2] , nums[i-1] , nums[i]
            if (a+b > c) and (b+c > a) and (c+a>b):
                per = a+b+c
                return per
        
        return max_per