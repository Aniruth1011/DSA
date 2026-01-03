class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = set(nums1)
        l2 = set(nums2)
        res = set()
        for i in l1:
            if i in l2:
                res.add(i)
        
        return list(res)