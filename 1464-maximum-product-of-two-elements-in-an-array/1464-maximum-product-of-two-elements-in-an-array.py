class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prod_matrix = [] 
        heapq.heapify(prod_matrix)

        for i in range(0 , n):
            for j in range(0 , n):
                if i!=j:
                    prod = (nums[i] - 1) * (nums[j]-1)
                    heapq.heappush(prod_matrix , -prod )
        
        prod = heapq.heappop(prod_matrix)
        return -prod
                