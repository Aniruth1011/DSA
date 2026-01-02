class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m , n = len(matrix) , len(matrix[0])
        #print(m , n)
        self.m , self.n = m , n
        prefix_sum = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            prefix_sum[i][0] = matrix[i][0]
            for j in range(1 , n):
                prefix_sum[i][j] = prefix_sum[i][j-1] + matrix[i][j]
        
        self.prefix_sum = prefix_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 1 and self.n == 1:
            return self.prefix_sum[0][0]
        s = 0
        for i in range(row1 , row2+1):
            if col1 == 0:
                s += self.prefix_sum[i][col2]
            else:
                s+= self.prefix_sum[i][col2] - self.prefix_sum[i][col1-1]
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)