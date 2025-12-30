class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows==2:
            return [[1] , [1 , 1]]
        
        answer = [[0 for i in range(j+1)] for j in range(numRows)]
        answer[0][0] = 1 
        answer[1][0] = 1 
        answer[1][1] = 1 

        for i in range(2 , numRows):
            for j in range(i+1):
                if j==0 or j==i:
                    answer[i][j] = answer[i-1][j-1]
                else:
                    answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        
        return answer