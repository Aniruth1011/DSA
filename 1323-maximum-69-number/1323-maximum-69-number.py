class Solution:
    def maximum69Number (self, num: int) -> int:
        if "6" in str(num):
            idx = str(num).index("6")
            l = list(str(num))
            l[idx] = "9"

            return int("".join(l))
        
        return num