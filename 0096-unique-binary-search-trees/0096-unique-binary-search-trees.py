class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def count(start , end):
            if start > end:
                return 1 
            
            if (start , end) in memo:
                return memo[(start , end)]
            s = 0
            for i in range(start , end+1):
                left_counts = count(start , i-1)
                right_counts = count(i+1 , end)
                s+= (left_counts * right_counts)
            
            memo[(start , end)] = s
            return s
        
        return count(1 , n)
