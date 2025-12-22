class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        if n==0:
            return [-1 , -1]
        elif n==1:
            if nums[0] == target:
                return [0 , 0]
            else:
                return [-1,-1]
        elif n==2:
            if nums[0] == nums[1] :
                if nums[0] == target:
                    return [0,1]
            else:
                if nums[0] == target:
                    return [0,0]
                elif nums[1] == target:
                    return [1,1]
                return [-1,-1]
        l = 0 
        r = n-1 

        while (l<=r):
            med = (l+r)//2 
            if (nums[med] == target):
                value1 = med
                value2 = med
                res = []
                if med >0:
                    while (nums[value1]==nums[value1-1]):
                        value1-=1
                        if value1 == 0:
                            break
                starting = value1 
                if med < n-1:
                    while (nums[value2] == nums[value2+1]):
                        value2+=1 
                        if value2 == n-1:
                            break 
                ending = value2 
                return [starting , ending] 

            elif (nums[med] < target):
                l = med+1
            else:
                r = med-1
        return [-1,-1]