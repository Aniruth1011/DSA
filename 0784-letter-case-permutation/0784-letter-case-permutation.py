class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(start , path):
            if start == len(s):
                result.append("".join(path))
                return 

            char = s[start]
            if char.isdigit():
                path.append(char)
                backtrack(start+1 , path)
                path.pop()
            else:
                path.append(char.upper())
                backtrack(start + 1 , path)
                path.pop()

                path.append(char.lower())
                backtrack(start+1, path)
                path.pop()
        
        backtrack(0 , [])
        return result 