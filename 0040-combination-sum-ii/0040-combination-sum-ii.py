class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        def backtrack(path , sum_of_num , start):
            if sum_of_num == target:
                results.append(path[:])
                return 
            
            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue 
                if (sum_of_num + candidates[i]) > target:
                    continue
                path.append(candidates[i])
                backtrack(path , sum_of_num + candidates[i] , i+1)
                path.pop()
        
        backtrack([] , 0 , 0)
        return results
