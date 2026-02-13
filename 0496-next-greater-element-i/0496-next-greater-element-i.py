class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        result = []
        stack = []
        next_greater = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                prev = stack.pop() 
                next_greater[prev] = nums2[i]
            stack.append(nums2[i])
        return [next_greater.get(num, -1) for num in nums1]
