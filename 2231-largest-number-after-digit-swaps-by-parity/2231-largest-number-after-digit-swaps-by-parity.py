class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(map(int, str(num)))
        
        evens = sorted([d for d in digits if d % 2 == 0], reverse=True)
        odds = sorted([d for d in digits if d % 2 == 1], reverse=True)
        
        res = []
        e = o = 0
        
        for d in digits:
            if d % 2 == 0:
                res.append(evens[e])
                e += 1
            else:
                res.append(odds[o])
                o += 1
        
        return int("".join(map(str, res)))
