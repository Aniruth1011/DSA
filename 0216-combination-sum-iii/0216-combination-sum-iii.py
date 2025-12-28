class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start , path , s):
            if len(path)==k and s ==n:
                result.append(path[:]) 
                return 
            
            for i in range(start , 10):
                if (s+i)>n:
                    break
                path.append(i)
                backtrack(i+1 , path , s + i)
                path.pop()
            
        backtrack(1 , [] , 0)
        return result 
