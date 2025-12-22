class Solution:
    def partition(self , nums ,  left , right):
        pivot_element = nums[right]
        i = left - 1
        for j in range(left , right):
            if nums[j] <= pivot_element:
                i+=1 
                nums[i] , nums[j] = nums[j] , nums[i]
        nums[i+1] , nums[right] = nums[right] , nums[i+1]
        return i+1 

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        high = len(nums)-1 
        def quicksort(nums , low , high):
            if low < high:
                pi = self.partition(nums, low, high)
                quicksort(nums, low, pi - 1)    
                quicksort(nums, pi + 1, high)  
        quicksort(nums , 0 , high)