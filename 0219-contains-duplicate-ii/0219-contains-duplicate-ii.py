class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0 
        j = 0 
        seen = set()
        while (j < n):
            if nums[j] in seen:
                return True 
            seen.add(nums[j])
            if j - i >=k:
                seen.remove(nums[i])
                i+=1
            j+=1
        return False