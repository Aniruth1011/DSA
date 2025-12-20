class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <=1:
            return n
        l = 0 
        r = 0 
        seen_chars = set()
        maxlen = 0
        while (r < n):
            ch = s[r]
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l+=1 
            seen_chars.add(ch)
            maxlen = max(maxlen , r-l+1)
            r+=1 
        return maxlen

        #     substring = s[l:r+1]
        #     if len(substring) == len(set(substring)):
        #         #No repeating characters
        #         maxlen = max(maxlen , r-l+1)
        #         r+=1
            
        #     while(len(s[l:r+1])!=len(set(s[l:r+1]))):
        #         l+=1
            
        # return maxlen
