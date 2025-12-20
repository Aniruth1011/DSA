from collections import defaultdict 
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        if n<=1:
            return n
        num_substrings = int(n * (n+1) / 2) 
        l = 0 
        r = 0 
        c = 0
        dic = defaultdict(int)
        se = set()
        while (r < n):
            ch = s[r]
            dic[ch]+=1 
            while len(dic)>2:

                dic[s[l]]-=1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l+=1 
            c += (r-l+1)

            r+=1 
        #print(num_substrings , c)
        return num_substrings - c