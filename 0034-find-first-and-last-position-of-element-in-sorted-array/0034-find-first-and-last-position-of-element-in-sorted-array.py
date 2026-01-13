class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0 
        right = n-1 
        idx = -1
        while left <= right:
            mid = (left + right)//2 
            if nums[mid] == target:
                idx = mid  
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1 
        
        if idx == -1:
            return [-1 , -1]
        base_idx1 = idx  
        while (base_idx1>=0) and (nums[base_idx1] == target) : 
            base_idx1-=1

        base_idx2 = idx 
        while (base_idx2<n) and (nums[base_idx2] == target) : 
            base_idx2+=1
        
        return [base_idx1+1 , base_idx2-1]

