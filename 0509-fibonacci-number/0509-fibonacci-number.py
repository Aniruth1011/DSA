class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n 
        prev_2 = 0
        prev_1 = 1 
        for i in range(2,n+1):
            next_val = prev_1 + prev_2 
            prev_1 , prev_2 = next_val, prev_1 
        return next_val

