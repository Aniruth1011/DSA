from collections import Counter
import math
class Solution:
    def reorganizeString(self, s: str) -> str:

        n = len(s)
        counter = Counter(s)
        max_heap = [(-frequency , character) for  character , frequency in counter.items() ]
        heapq.heapify(max_heap)

        max_occuring_char_freq , ch = max_heap[0]
        print(-max_occuring_char_freq , n , n//2)
        if (-max_occuring_char_freq) > (n + 1) // 2:
            return ""
        prev_char = None 
        prev_freq = 0
        answer = ""
        while max_heap:
            freq , char = heapq.heappop(max_heap)
            answer+=(char)
            freq += 1  
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            prev_freq, prev_char = freq, char

        return answer

                
