class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)

        nums1.sort()
        nums2.sort()
        possible_answers = []
        for i in range(l1):
            for j in range(i+1 , l1):
                temp = nums1[:]
                temp.pop(j)
                temp.pop(i)
                diff = nums2[0] - temp[0]
                if all(nums2[k] - temp[k] == diff for k in range(l2)):
                    possible_answers.append(diff)
        
        return min(possible_answers)