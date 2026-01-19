class Solution:
    def binary_search(self , target , num):
        l = 0 
        r = len(target) - 1
        while (l<r):
            mid = (l+r)//2 
            if target[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(1 , n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        min_len = float('inf')
        for i in range(n):
            required = prefix_sum[i] + target
            j = self.binary_search(prefix_sum , required)
            if j <= n and prefix_sum[j] >= required:
                min_len = min(min_len, j - i)
        
        if min_len == float('inf'):
            return 0 
        return min_len 

