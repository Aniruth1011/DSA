class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            number = nums1[i]
            for j in range(len(nums2)):
                if number == nums2[j]:
                    flag = True
                    for k in range(j+1 , len(nums2)):
                        if nums2[k] > number and flag:
                            result.append(nums2[k])
                            flag = False 
                    if flag:
                        result.append(-1)
        return result 
        