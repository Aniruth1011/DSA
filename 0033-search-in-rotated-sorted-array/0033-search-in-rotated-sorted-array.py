class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums) 
        if n == 1:
            if nums[0] == target:
                return 0 
            return -1 
        l = 0 
        r = n -1

        while (l<=r):
            median = (l+r)//2 
            if (nums[median]) == target:
                return median 
            if (nums[l] <= nums[median]):
                if (nums[l] <= target) and (target < nums[median]):
                    r = median - 1 
                else:
                    l = median + 1
            else:
                if (nums[median] < target) and (target<=nums[r]):
                    l = median + 1 
                else:
                    r = median - 1
        return -1