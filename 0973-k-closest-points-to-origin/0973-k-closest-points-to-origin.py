class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = [  ( ((x1**2) + (y1**2)), idx) for idx ,  (x1 , y1) in enumerate(points) ]
        heapq.heapify(distance)

        list_of_points = heapq.nsmallest(k , distance)
        result = []
        for point, idx in list_of_points:
            result.append(points[idx])
        
        return result 
