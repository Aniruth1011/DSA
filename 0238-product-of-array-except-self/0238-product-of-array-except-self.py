class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for i in range(n)]

        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]
        print(result)
        val = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * val 
            val = val * nums[i]
        
        return result

"""
[1,1,2,3]

"""