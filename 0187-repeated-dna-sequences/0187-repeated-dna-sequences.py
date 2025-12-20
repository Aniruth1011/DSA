class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n<10:
            return []
        dic = set()
        l = 0 
        r = 9 
        ans = set()
        while (r<n):
            sub = s[l:r+1]
            if sub in dic:
                ans.add(sub)
            else:
                dic.add(sub)
            l+=1
            r+=1
        return list(ans)