class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        l = [0 for i in range(n)]
        r = [0 for i in range(n)]
        max_c = 0 
        for i in range(n):
            if s[i]=='0' and i==0:
                l[i] = 1
            elif s[i]=='0' and i>0:
                l[i] = l[i-1] + 1
            else:
                l[i] = l[i-1]
        if s[n-1]=='1':
            r[n-1] = 1
        for i in range(n-2,-1,-1):
            if s[i]=='1':
                r[i] = r[i+1] + 1
            else:
                r[i] = r[i+1]
        print(l)
        print(r)
        return max(l[i] + r[i + 1] for i in range(n - 1))