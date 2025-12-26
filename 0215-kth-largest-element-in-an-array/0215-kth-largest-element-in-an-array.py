class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rev_nums = [-i for i in nums]
        heapq.heapify(rev_nums)
        for i in range(k):
            val = heapq.heappop(rev_nums)
        
        return -val 
