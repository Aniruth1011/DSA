class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        matrix = [[-i for i in row ] for row in grid]
        for i in range(n):
            heapq.heapify(matrix[i])
        c = 0

        while any(matrix[row] for row in range(n)):
            res = []
            for row in range(n):
                heap = matrix[row]
                _ = heapq.heappop(heap)
                res.append(-_)
                matrix[row] = heap 
            c+=max(res)                
        return c 
        