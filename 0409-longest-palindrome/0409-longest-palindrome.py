import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        l = 0
        odd = False
        for count in counter.values():
            if count%2==0:
                l+=count 
            else:
                l+=(count-1)
                odd = True
        if odd:
            return l+1
        return l 