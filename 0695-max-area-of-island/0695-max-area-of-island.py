class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row , col = len(grid) , len(grid[0])
        def dfs(r , c ):

            if (r < 0) or (r>=row) or (c<0) or (c>=col) or grid[r][c]==0:
                return 0
            
            grid[r][c] = 0
            count=1
            count+= dfs(r-1 , c ) # ,  count )
            count+= dfs(r+1 , c ) #,  count)
            count+= dfs(r , c-1 ) #,  count)
            count+= dfs(r , c+1 ) # ,  count)

            return count 
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = dfs(i , j ) #, 0)
                    print(area , max_area , i , j)
                    max_area = max(max_area , area)

        return max_area
