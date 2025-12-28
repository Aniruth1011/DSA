class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(start , path):
            if len(path) == len(s):
                result.append("".join(path))
                return 

            for end in range(start, len(s)):
                char = s[end]
                if char in "0123456789":
                    path.append(char)
                    backtrack(end+1 , path)
                    path.pop()
                else:
                    path.append(char)
                    backtrack(end+1 , path)
                    path.pop()

                    if char.islower():
                        path.append(char.upper())
                        backtrack(end + 1 , path)
                        path.pop()
                    else:
                        path.append(char.lower())
                        backtrack(end+1, path)
                        path.pop()
        
        backtrack(0 , [])
        return result 