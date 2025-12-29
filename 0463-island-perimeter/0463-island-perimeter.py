class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimiter = 0
        rows , cols = len(grid) , len(grid[0])
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == 1:
                    perimiter += 4
                    if row>0 and grid[row-1][column] == 1:
                        perimiter-=2 
                    if column > 0 and grid[row][column-1] == 1:
                        perimiter-=2 
        return perimiter