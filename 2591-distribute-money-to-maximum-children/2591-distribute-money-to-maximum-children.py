class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if children > money:
            return -1 
        
        n = (8*children) - money 

        if n<=0:
            return children - (n<0)
        
        num , rem = divmod(money - children , 7)

        return num - ((num, rem) == (children - 1, 3))
