class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        s=0
        for i , num in enumerate(nums):
            s+=num 
            rem = s% k 
            if rem in dic:
                if i-dic[rem]>=2:
                    return True 
            else:
                dic[rem] = i 
        return False