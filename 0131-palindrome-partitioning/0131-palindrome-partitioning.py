class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispalindrome(s):
            if s == s[::-1]:
                return True 
            return False 
        
        result = []
        def backtrack(start , path):
            if start == len(s):
                result.append(path[:])
                return 
            
            for end in range(start+1 , len(s)+1):
                if ispalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end , path)
                    path.pop()
        
        backtrack(0 , [])
        return result 
