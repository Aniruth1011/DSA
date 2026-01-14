class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        n = len(nums)
        used = [False for i in range(n)]
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            
            for i in range(0 , n):
                if used[i]:
                    continue 
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                used[i] = False
                path.pop()
        
        backtrack([])
        return result 
