from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <=1:
            return n
        l = 0 
        r = 0 
        types = defaultdict(int)
        maxlen = 0
        while (r < n):
            type_ = fruits[r]
            types[type_]+=1 
            while len(types) > 2:
                types[fruits[l]]-=1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l+=1
            maxlen = max(maxlen , r - l +1)
            r+=1
        return maxlen
