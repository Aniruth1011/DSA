import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg_gifts = [-i for i in gifts]
        heapq.heapify(neg_gifts)

        for i in range(k):
            val = heapq.heappop(neg_gifts)

            sqrt = int((-val) ** 0.5)
            heapq.heappush(neg_gifts , -sqrt)
        
        return -sum(neg_gifts)
