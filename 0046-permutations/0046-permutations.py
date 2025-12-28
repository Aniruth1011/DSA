class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(path , used):

            if len(path) == len(nums):
                results.append(path[:])
                return 
            for j in range(len(nums)):
                if not used[j]:
                    path.append(nums[j])
                    used[j] = True
                    backtrack(path , used)
                    path.pop()
                    used[j] = False
            
        backtrack([] , [False] * len(nums))
        return results 
