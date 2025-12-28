class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        results = []

        def backtrack(combination , num_open , num_close ):

            if len(combination)//2 == n:
                results.append("".join(combination))
                return 
            if num_open < n:
                combination.append("(")
                backtrack(combination , num_open +1 , num_close )
                combination.pop()
            
            if num_close < num_open:
                combination.append(")")
                backtrack(combination , num_open , num_close+1)
                combination.pop()

                    

        backtrack([] , 0 , 0 )
        return results
        