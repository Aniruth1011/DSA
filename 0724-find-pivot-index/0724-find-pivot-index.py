class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)
        prefix_sum = [0] * ( n + 1 )
        for i in range(1 , n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        for i in range(1 , n+1):
            print(prefix_sum[i-1] - prefix_sum[0]  , prefix_sum[n] - prefix_sum[i])
            if  ( prefix_sum[i-1] - prefix_sum[0] ) == prefix_sum[n] - prefix_sum[i]:
                return i-1
        return -1 
