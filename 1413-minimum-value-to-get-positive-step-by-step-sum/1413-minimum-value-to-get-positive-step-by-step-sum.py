class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i = 1
        flag = False
        while True:
            k = i
            for j in nums:
                k+=j 
                if k < 1:
                    flag = True 
                    break 
            
            if flag == False:
                break 
            i+=1 
            flag = False
            
        return i 

