class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []
        def backtrack(path , sum_of_num , start):
            if sum_of_num > target:
                return 
            if sum_of_num == target:
                results.append(path[:])
                return 
            
            for i in range(start , len(candidates)):
                path.append(candidates[i])
                backtrack(path , sum_of_num + candidates[i] , i)
                path.pop()
        
        backtrack([] , 0 , 0)
        return results
            