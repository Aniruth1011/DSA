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

        if all(x == 0 for row in grid for x in row):
            return Node(0 , True , None , None , None , None)
        elif all(x == 1 for row in grid for x in row):
            return Node(1 , True , None , None , None , None)  
        else:
            #Recursive case 
            isleaf = False 
            val = 1 #Arbitrarily selected 
            n = len(grid)
            topleft = self.construct([row[:n//2] for row in grid[:n//2]]) 
            topright = self.construct([row[n//2:] for row in grid[:n//2]]) 
            bottomleft = self.construct([row[:n//2] for row in grid[n//2:]]) 
            bottomright = self.construct([row[n//2:] for row in grid[n//2:]]) 

            return Node(val , isleaf , topleft , topright , bottomleft , bottomright)
        
