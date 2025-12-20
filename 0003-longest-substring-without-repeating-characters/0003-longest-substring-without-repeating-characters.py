class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        r = 0 
        n = len(s)
        maxlen = 0
        while (r < n):
            substring = s[l:r+1]
            if len(substring) == len(set(substring)):
                #No repeating characters
                maxlen = max(maxlen , r-l+1)
                r+=1
            
            while(len(s[l:r+1])!=len(set(s[l:r+1]))):
                l+=1
            
        return maxlen
