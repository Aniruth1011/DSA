"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        prefix_sum = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            for j in range(n):
                prefix_sum[i+1][j+1] = int(grid[i][j]) + prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]
        
        def get_prefix_sum(r1 , c1 , r2 , c2):
            return prefix_sum[r2][c2] - prefix_sum[r2 ][c1] - prefix_sum[r1][c2] + prefix_sum[r1][c1]
            
        def build(r1 , c1 , r2 , c2):
            if get_prefix_sum(r1 , c1, r2 , c2) == 0:
                return Node(0 , True , None , None , None , None)
            elif get_prefix_sum(r1 , c1, r2 , c2) == (r2-r1)**2:
                return Node(1 , True , None , None , None , None)  
            else:
                #Recursive case 
                isleaf = False 
                val = 1 #Arbitrarily selected 
                n = len(grid)
                width = r2 - r1
                mid_r = r1 + width//2 
                mid_c = c1 + width//2 
                topleft = build(r1 , c1 , mid_r , mid_c)
                topright = build(r1, mid_c, mid_r, c2 )
                bottomleft = build(mid_r , c1 , r2 , mid_c )
                bottomright = build(mid_r, mid_c, r2, c2)
            
                return Node(val , isleaf , topleft , topright , bottomleft , bottomright)
        
        return build(0 , 0 , len(grid) , len(grid))