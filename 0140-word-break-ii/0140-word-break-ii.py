class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        def backtrack(start , sentence):
            if start == len(s):
                result.append(" ".join(sentence))
            for end in range(start + 1, len(s)+1):
                word = s[start:end]
                if word in wordDict:
                    sentence.append(word)
                    backtrack(end , sentence)
                    sentence.pop()
            
        backtrack(0 , [])
        return result 

        