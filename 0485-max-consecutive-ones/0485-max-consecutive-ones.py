class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = 0 
        l = 0 
        max_l = 0
        for i in range(len(nums)):
            if nums[i]==0:
                max_l = max(max_l , l) 
                l = 0
            else:
                if i>0 and nums[i-1]==1:
                    l+=1
                elif i>0 and nums[i-1]!=1:
                    s = i 
                    l+=1
                elif i==0:
                    s = i
                    l+=1
        
        return max(max_l , l)
