class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if (children > money):
            return -1
        child = [1 for i in range(children)]
        money-=children 
        i = 0
        while money>0:
            if (child[i] < 8) and money>=8:
                money-=(8 - child[i]) 
                child[i] = 8 

            if i==children-1:
                if money > 0:
                    if child[i]+money!=4:
                        child[i]+=money 
                        money = 0
                    else:
                        child[i-1]+=money 
                        money=0 
            i+=1
        ct = 0 
        print(child)
        for i in child:
            if i==8:
                ct+=1 
        return ct 