class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        n = len(nums)
        if nums[0]>0:
            return []
        for i in range(n):
            num = nums[i]
            if i > 0 and (nums[i] == nums[i-1]):
                continue 
            target = -num 
            start = i+1 
            end = n - 1 
            while (start < end ):
                num1 = nums[start]
                num2 = nums[end]
                if ((num1 + num2) == target):
                    triplets.append([ num , num1 , num2 ])
                    start+=1
                    end-=1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif (num1 + num2) > target:
                    end-=1
                else:
                    start+=1  
    
            #print(f"{i} completed")
        return triplets