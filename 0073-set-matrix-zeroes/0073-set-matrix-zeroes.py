class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        original_zeros = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    original_zeros.append([i , j])
        
        for (row , col) in original_zeros:
            for c in range(n):
                matrix[row][c] = 0 
            for r in range(m):
                matrix[r][col] = 0 
        