class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def search(x , y ,  letter_idx):
            if letter_idx == len(word):
                return True 
            
            if (x<0) or (y<0) or (x>=m) or (y>=n):
                return False 
            
            if board[x][y]!=word[letter_idx]:
                return False 
            
            temp = board[x][y]
            board[x][y] = "**"
            ok = search(x+1 , y , letter_idx+1) or search(x-1 , y , letter_idx+1) or search(x , y+1, letter_idx+1) or search(x , y-1, letter_idx+1)
            board[x][y]=temp 
            return ok 
        
        for i in range(m):
            for j in range(n):
                if search(i , j , 0):
                    return True 
        return False
