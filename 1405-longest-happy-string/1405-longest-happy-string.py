import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []
        if a>0:
            heap.append((-a , 'a'))
        if b>0:
            heap.append((-b , 'b'))
        if c>0:
            heap.append((-c , 'c'))

        heapq.heapify(heap) 
        result = ""
        while heap:
            freq , ch = heapq.heappop(heap)
            if len(result)>=2 and (result[-1] == result[-2]) and (result[-2] == ch):
                if not heap:
                    break 
                #illegal substring possible
                second_freq , ch2 = heapq.heappop(heap)
                result+=ch2 
                second_freq+=1
                if second_freq < 0:
                    heapq.heappush(heap,( second_freq  , ch2))
                heapq.heappush(heap,(freq , ch))
            else:
                result+=ch 
                freq+=1
                if freq < 0:
                    heapq.heappush(heap,(freq , ch))
            print(result)
        
        return result
            
            