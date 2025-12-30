class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        starting_colour = image[sr][sc]
        if starting_colour == color:
            return image

        m , n = len(image) , len(image[0])
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n :
                return 
            if image[x][y]!= starting_colour:
                return 
            
            image[x][y] = color 
            dfs(x-1 , y)
            dfs(x+1 , y)
            dfs(x , y-1)
            dfs(x , y+1)

        
        dfs(sr , sc)
        return image