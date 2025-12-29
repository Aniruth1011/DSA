class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def backtrack(path , n_open , n_closed):
            if (n_open + n_closed) == 2*n:
                result.append("".join(path))
                return 

            if n_open < n:
                path.append("(")
                backtrack(path , n_open+1 , n_closed)
                path.pop()

            if n_closed < n_open : 
                path.append(")")
                backtrack(path , n_open , n_closed + 1)
                path.pop()
        
        backtrack([] , 0 , 0)
        return result 

