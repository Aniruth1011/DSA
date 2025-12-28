class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start , path):
            if len(path)==k and sum(path)==n:
                result.append(path[:]) 
                return 
            
            for i in range(start , 10):
                path.append(i)
                backtrack(i+1 , path)
                path.pop()
            
        backtrack(1 , [])
        return result 
