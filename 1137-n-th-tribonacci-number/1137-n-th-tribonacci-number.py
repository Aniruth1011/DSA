class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0 
        if n<=2:
            return 1
        T3 = 0
        T2 = 1
        T1 = 1 
        for i in range(3,n+1):
            T1,T2,T3 = T1 + T2 + T3 , T1 , T2
        return T1
