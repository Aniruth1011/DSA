class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0 
        n = len(chars)
        c = 0
        k = 0
        i = 0
        while k < n:
            char = chars[k]
            j = k
            while (j<n-1) and (chars[j+1] == chars[j]):
                print(j , n)
                j+=1 
            count = j - k + 1 
            chars[i] = char 
            i+=1
            if count > 1:
                for m in str(count):
                    chars[i] = m 
                    i+=1
            k = j + 1

        return i