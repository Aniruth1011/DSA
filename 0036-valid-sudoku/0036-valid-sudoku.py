class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for i in range(9)]
        column = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in row[i]:
                        return False 
                    row[i].add(board[i][j])
        
        for i in range(9):
            for j in range(9):
                if board[j][i]!=".":
                    if board[j][i] in column[i]:
                        return False 
                    column[i].add(board[j][i])
        
        for i in range(9):
            for j in range(9):
                box_number = (i//3) + (j//3)*3 
                if board[i][j]!=".":
                    if board[i][j] in boxes[box_number]:
                        return False 
                    boxes[box_number].add(board[i][j])
        return True 

