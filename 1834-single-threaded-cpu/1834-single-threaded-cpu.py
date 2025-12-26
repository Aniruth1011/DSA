class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        sorted_tasks = [(start_time , processing_time , idx) for idx , (start_time , processing_time) in enumerate(tasks)]
        sorted_tasks.sort()

        result = []
        min_heap = []

        t = 0 
        num_completed = 0 
        num_tasks = len(tasks)

        while (num_completed < num_tasks) or (min_heap):
            if not min_heap and (t < sorted_tasks[num_completed][0]):
                t = sorted_tasks[num_completed][0] 
            
            while (num_completed < num_tasks) and (sorted_tasks[num_completed][0] <=t) : 
                start_time , processing_time , idx = sorted_tasks[num_completed]
                heapq.heappush(min_heap, (processing_time, idx))
                num_completed+=1 
            
            processing_time, idx = heapq.heappop(min_heap)
            t += processing_time
            result.append(idx)
        
        return result
"""
min heap sort based on enqueue time 
[[1,2] , [2,4] , [3,2] , [4,1]]

current_time = 
"""