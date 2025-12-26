class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        sorted_tasks = sorted([(start_time , processing_time , idx) for idx , (start_time , processing_time) in enumerate(tasks)])

        result = []
        min_heap = []

        t = 0 
        num_waiting = 0 
        num_tasks = len(tasks)

        while (num_waiting < num_tasks) or (min_heap):
            if not min_heap and (t < sorted_tasks[num_waiting][0]):
                t = sorted_tasks[num_waiting][0] 
            
            while (num_waiting < num_tasks) and (sorted_tasks[num_waiting][0] <=t) : 
                start_time , processing_time , idx = sorted_tasks[num_waiting]
                heapq.heappush(min_heap, (processing_time, idx))
                num_waiting+=1 
            
            processing_time, idx = heapq.heappop(min_heap)
            t += processing_time
            result.append(idx)
        
        return result
"""
min heap sort based on enqueue time 
[[1,2] , [2,4] , [3,2] , [4,1]]

current_time = 
"""