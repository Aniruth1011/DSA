from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None or not grid[0]:
            return 

        queue = deque()
        row , column = len(grid) , len(grid[0])
        minute = 0
        max_minutes = row * column

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    queue.append((i , j , minute))
        
        directions = ((-1, 0) , (1 , 0) , (0,1) , (0,-1))
        t_ = 0
        while queue:
            r , c , t = queue.popleft()
            t_ = max(t , t_)
            for (dr , dc) in directions:
                r_n , c_n = r+dr , c+dc
                if (0<=r_n<row) and (0<=c_n<column) and grid[r_n][c_n]==1:
                    grid[r_n][c_n] = 2 
                    queue.append((r_n , c_n , t+1))
        
        if any(i == 1  for row in grid for i in row):
            return -1
        return t_
