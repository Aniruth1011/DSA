class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        r = 0 

        n = len(nums)

        numones = 0 
        numzeros = 0

        maxlen = 0
        
        while (r < n):
            element = nums[r]
            if element==1:
                numones+=1
            else:
                numzeros+=1
            if (numzeros>k):
                if nums[l] == 0:
                    numzeros-=1
                l+=1
            maxlen = max(maxlen , r-l+1)
            #print(l , r , maxlen , numzeros , numones)
            r+=1
        
        return maxlen