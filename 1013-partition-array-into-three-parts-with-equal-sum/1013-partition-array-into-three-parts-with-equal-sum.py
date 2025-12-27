class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        s = sum(arr)
        if s%3!=0:
            return False 
        
        target = s//3 
        sum_ = 0 
        c = 0 
        for i in arr:
            sum_+=i 
            if (sum_==target):
                sum_ = 0 
                c+=1 
        
        if (c>=3):
            return True 
        return False