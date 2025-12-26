class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_five = 0 
        num_ten = 0 
        num_twenty = 0 

        for i in bills:
            if i == 5:
                num_five+=1
            elif i == 10:
                if num_five>0:
                    num_five-=1
                    num_ten+=1
                else:
                    return False 
            elif i==20:
                if num_five > 0 and num_ten > 0:
                    num_five-=1
                    num_ten-=1 
                elif (num_ten == 0) and (num_five>=3):
                    num_five-=3
                else:
                    return False
        return True