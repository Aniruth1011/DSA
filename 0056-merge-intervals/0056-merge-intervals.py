class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        if n==1:
            return intervals 
        results = []
        l , r = intervals[0][0] , intervals[0][1]
        i = 1
        while i < n:
            new_l , new_r = intervals[i][0] , intervals[i][1]
            if l <= new_l <= new_r <= r:
                pass                         
            elif l <= new_l <= r <= new_r:
                r = new_r                    
            else:
                results.append([l, r])     
                l, r = new_l, new_r
            i += 1
        results.append([l, r])
        return results