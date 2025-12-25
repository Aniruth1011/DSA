import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = []
        for row in mat:
            strength.append(sum(row))

        min_heap = [(stre , i) for i , stre in enumerate(strength)]
        heapq.heapify(min_heap)
        result = []
        ct = 0
        while min_heap:
            stre , idx = heapq.heappop(min_heap)
            result.append(idx)
            ct+=1 
            if ct == k:
                break
        
        return result