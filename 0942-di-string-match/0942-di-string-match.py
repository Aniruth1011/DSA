class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        n = len(s)
        low = 0 
        high = n
        output = []
        for char in s:
            if char == "I":
                output.append(low)
                low+=1
            else:
                output.append(high)
                high-=1
        
        output.append(low)
        return output