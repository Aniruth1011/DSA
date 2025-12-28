class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits is None:
            return []
        d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []
        def backtrack(idx , path):
            if idx == len(digits):
                result.append("".join(path))
                return 
            letters = d[digits[idx]]
            for letter in letters:
                path.append(letter)
                backtrack(idx+1 , path)
                path.pop()
        backtrack(0 , [])

        return result 
